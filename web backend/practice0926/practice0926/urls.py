"""practice0926 프로젝트의 root URL Configuration 파일.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# URL 패턴을 작성할 때 필요한 함수, 모듈 불러오기.
from django.contrib import admin
from django.urls import path, include

from introduce import views


# URL 패턴(=요청 URL 주소값과 이를 처리할 함수명, path 함수로 작성)
# 을 등록하고 기록하는 목록 변수.
# 변수명이 반드시 urlpatterns 인 경우만 인식함.
urlpatterns = [
    # 관리자 페이지 접속 URL 패턴.
    path('admin/', admin.site.urls),
    # 요청 URL이 호스트+포트로만 구성된 경우, home 함수 실행.
    path('', views.home),
    
    # 요청 URL이 /intro/... 인 경우, introduce 앱의 URLconf 파일로 처리.
    path('intro/', include('introduce.urls')),
    # 요청 URL이 /back/... 인 경우, background 앱의 URLconf 파일로 처리.
    path('back/', include('background.urls')),
    # 요청 URL이 /gram/... 인 경우, grammar 앱의 URLconf 파일로 처리.
    path('gram/', include('grammar.urls')),
]
