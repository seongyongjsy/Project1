# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def create_user(request):
    """사용자 등록 페이지로 연결시켜주는 뷰 함수."""
    return render(request, "user/create_user.html")
