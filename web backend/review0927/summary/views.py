from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
def home(request):
    """홈 화면으로 이동하는 뷰 함수."""
    
    # 뷰 함수에서 실행할 기능(데이터 검사, 가공 처리 등)을 작성.
    print("summary 앱의 home 뷰 함수 실행.")

    # HttpResponse 객체를 이용해서 문자열을 응답.
    # return HttpResponse("홈 화면 접속.")

    # HttpResponse 객체를 이용해서 HTML 태그 형태로 작성된 문자열을 응답.
    html = """
    <h1>장고 복습용 연습 프로젝트</h1>
    <a href='/summary/setup'>가상환경 설정 및 장고 설치</a><br>
    <a href='/summary/project-app'>프로젝트 및 앱 생성</a><br>
    <a href='/summary/request-response'>요청-응답 처리</a><br>
    """
    return HttpResponse(html)


def setup(request):
    """가상환경 설정 및 장고 설치 페이지로 이동하는 뷰 함수."""

    # 템플릿을 응답하기 위해 템플릿을 가져오기.
    template = loader.get_template("summary/setup.html")
    # 서버에서 클라이언트로 전달할 데이터.
    # context = {'a': 10, 'b': 20}
    context = {}

    return HttpResponse(template.render(context, request))


def proj_app(request):
    """프로젝트 및 앱 생성 페이지로 이동하는 뷰 함수."""
    
    # 서버에서 클라이언트로 전달할 데이터.
    context = {'a': 'hello', 'b': 'hi'}
    
    return render(request, "summary/project-app.html", context)


def req_res(request):
    """요청-응답 처리 페이지로 이동하는 뷰 함수."""
    return render(request, "summary/request-response.html")

def url_pattern_test(request, number):
    """요청 시 URL 패턴에 데이터를 추가해서 보내는 방식 테스트 뷰 함수."""
    print(f"전달된 변수: {number=}")
    return HttpResponse("통신 성공?")

def keyword_test(request, a, b):
    """요청 시 키워드 인수 데이터를 추가해서 보내는 방식 테스트 뷰 함수."""
    print(f"전달된 데이터: {a=}, {b=}")
    return HttpResponse("통신 성공??")

def httpreq_test(request):
    """요청 시 HttpRequest 객체를 통해 데이터를 전달하는 방식 테스트 뷰 함수."""
    if request.GET:
        print("GET 요청 처리 실행")
        if len(request.GET) > 0:
            for key in request.GET.keys():
                print(f"key: {key}, value: {request.GET[key]}")
        else:
            print("전달된 데이터 없음.")
    elif request.POST:
        print("POST 요청 처리 실행")
    return HttpResponse("통신 성공???")
