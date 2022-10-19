from django.shortcuts import render

# Create your views here.
def login(request):
    user_list = [
        {'id': 'hong123', 'pw': '1234'},
        {'id': 'kim456', 'pw': '5678'},
    ]

    if request.POST:
        user_id = request.POST['userid']
        for user in user_list:
            if user_id == user['id']:
                if request.POST['userpw'] == user['pw']:
                    context = {'result': '로그인 성공'}
                    return render(request, "user/login.html", context)
        context = {'result': '로그인 실패'}
        return render(request, "user/login.html", context)
    else:
        return render(request, "user/login.html")
