"""summary 앱에서 사용할 하위 URL 구성 파일."""


from django.urls import path

from . import views


urlpatterns = [
    path('setting/', views.setting),
    path('model/', views.model),
]
