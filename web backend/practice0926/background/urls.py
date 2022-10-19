"""background 앱에서 관리하는 URLconf 파일."""


# URL 패턴을 작성할 때 필요한 함수 불러오기.
from django.urls import path

from . import views


# URL 패턴(=요청 URL 주소값과 이를 처리할 함수명, path 함수로 작성)
# 을 등록하고 기록하는 목록 변수.
# 변수명이 반드시 urlpatterns 인 경우만 인식함.
urlpatterns = [
    path('knowledge/', views.background_knowledge),
]