from django.urls import path

from . import views


app_name = 'polls' # polls 앱에 대한, URL 패턴 이름과 함께 사용하기 위한 네임스페이스.
urlpatterns = [
    path('list/', views.list, name='list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/choice/', views.choice, name='choice'), 
    path('<int:question_id>/result/', views.result, name='result'), 
]

