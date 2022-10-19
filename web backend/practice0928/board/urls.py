"""board 앱에서 사용할 하위 URL 구성 파일."""


from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_write),
]
