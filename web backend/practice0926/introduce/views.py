"""introduce 앱에서 요청을 처리할 뷰 함수를 작성하는 파일."""


from django.shortcuts import render


# Create your views here.
def home(request):
    """홈 화면으로 이동하는 뷰 함수."""
    return render(request, "introduce/home.html")


def introduce_django(request):
    """장고 개요 페이지로 이동하는 뷰 함수."""
    return render(request, "introduce/django.html")
