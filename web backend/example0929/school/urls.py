"""school 앱에서 사용하는 하위 URL 구성 파일."""


from django.urls import path

from . import views


urlpatterns = [
    path('student/list/', views.student_list),
    path('exam/list/', views.exam_list),
    path('exam/detail/', views.exam_detail),
    path('score/insert/', views.score_insert),
]
