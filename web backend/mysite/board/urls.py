from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.board_list),
    path('<int:board_num>/', views.board_detail),
]