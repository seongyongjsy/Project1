from django.urls import reverse 
from django.http import HTTPResponseRedirct
from django.shortcuts import render, redirect

from models import User

def login(request):
    if request.POST:
        # POST 방식으로 요청한 경우, 로그인 처리 후 홈 페이지로 이동.
        
        # 템플릿에서 전달한 데이터 확인.
        user_id = request.POST['id']
        user_pw = request.POST['pw']
        print(f"{user_id=}, {user_pw=}")

        # 데이터베이스에 일치하는 데이터가 존재하는지 검사.
        result = None
        try: 
            result = User.objects.get(pk=user_id, pw=user_pw)
        except:
            pass
        print("데이터베이스 조회 결과:", result)

        # 일치하는 데이터가 존재하면 세션에 사용자 ID 데이터를 저장.
        # 세션(session): 서버에 남아 데이터를 저장하는 객체.
        # 서버에 데이터를 저장하기 때문에 다른 페이지로 이동해도 데이터가 계속 남아있음.
        if result:
            request.session['user_id'] = user_id
            return redirect('/')
        else:
            # 일치하는 데이터가 존재하지 않는 경우, 다시 로그인 화면으로 이동.
            context = {
                'err_msg': 'ID/비밀번호를 확인해주세요.'
            }
            return render(request, "user/login.html")
            # return redirect('/user/login/')
    else:
        # GET 방식으로 요청한 경우, 로그인 페이지로 이동.
        return render(request, "user/login.html")


def logout(request):
    # 세션에서 로그인한 사용자의 ID 데이터를 삭제.
    del request.session['id']

    # return HTTPResponseRedirct('/') # '/' URL로 리다이렉트 명령.
    # return redirect('/')  # '/' URL로 리다이렉트 명령.
    # return redirect('home')   # 'home' URL 패턴 이름으로 리다이렉트 명령. 
    return redirect(reverse('home'))    # 'home' URL 패턴 이름에 대한 URL을 구해서 리다이렉트 명령.

# reverse('URL 패턴 이름'): 제시된 URL 패턴 이름에 대해 연결된 URL을 찾아서 문자열로 반환해주는 함수.
