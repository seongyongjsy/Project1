from django.urls import path

from . import views 


app_name = 'board'  # namespace: url 태그에서 사용하는, 앱 이름을 제시하는 변수 및 관련 문법.
urlpatterns = [
    path('list/', views.board_list, name='board_list'),
    path('<int:board_num>/', views.board_detail, name='board_detail'),
    path('update/', views.board_update, name='board_update'),
]
