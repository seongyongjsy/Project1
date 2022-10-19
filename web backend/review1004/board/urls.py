from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.board_list),
    path('<int:num>/', views.board_detail),
    # path('detail/', views.board_detail),
    path('summary/', views.board_summary),
]
