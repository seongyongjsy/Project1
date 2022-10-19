from django.shortcuts import render

# Create your views here.
def grammar_index(request):
    """장고 문법 목록 페이지로 이동하는 함수."""
    return render(request, "grammar/index.html")

def grammar_setup(request):
    """가상환경 설정 및 장고 설치 페이지로 이동하는 함수."""
    return render(request, "grammar/setup.html")

def grammar_command(request):
    """장고 명령어 페이지로 이동하는 함수."""
    return render(request, "grammar/command.html")

def grammar_req_res(request):
    """요청-응답 처리 관련 페이지로 이동하는 함수."""
    return render(request, "grammar/req-res.html")
