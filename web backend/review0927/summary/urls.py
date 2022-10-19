"""summary 앱에서 사용하는 하위 URL 구성 파일(URL configuration file)."""


# URL 패턴을 작성할 때 필요한 함수 불러오기.
from django.urls import path

# 현재 폴더(summary) 내 뷰 모듈(views.py) 불러오기.
from . import views


# URL 패턴 작성.
urlpatterns = [
    path('setup/', views.setup),
    path('project-app/', views.proj_app),
    path('request-response/', views.req_res),
    path('<int:number>/', views.url_pattern_test),
    path('keyword-test/', views.keyword_test, {'a': 10, 'b': 20}),
    path('httprequest-test/', views.httpreq_test),
]
