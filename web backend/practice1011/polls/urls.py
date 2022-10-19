from django.urls import path

from . import views


app_name = 'polls'  # polls 앱에 대한, URL 패턴 이름과 함께 사용하기 위한 네임스페이스.
urlpatterns = [
    # 설문 목록 페이지로 이동하는 URL 패턴.
    # 함수 기반 뷰를 사용해서 처리.
    # path('list/', views.list, name='list'),
    
    # /polls/list/ URL을 처리해서 설문 목록 페이지로 이동시키는 URL 패턴.
    # 클래스 기반 뷰를 사용해서 처리.
    path('list/', views.QuestionListView.as_view(), name='list'),

    # 설문 상세 페이지로 이동하는 URL 패턴.
    # 함수 기반 뷰를 사용해서 처리.
    # path('<int:question_id>/', views.detail, name='detail'),

    # /polls/<int:question_id>/ URL을 처리해서 설문 상세 페이지로 이동시키는 URL 패턴.
    # 클래스 기반 뷰를 사용해서 처리.
    path('<int:question_id>/', views.QuestionDetailView.as_view(), name='detail'),

    path('<int:question_id>/choice/', views.choice, name='choice'),  # 답변하기 기능을 실행하는 URL 패턴.
    path('<int:question_id>/result/', views.result, name='result'),  # 설문 결과 페이지로 이동하는 URL 패턴.

    # 질문 생성(설문 등록) 페이지 이동 및 데이터베이스 처리를 담당하는 URL 패턴.
    path('regist/', views.QuestionCreateView.as_view(), name='create'),

    # 질문 수정(설문 변경) 페이지 이동 및 데이터베이스 처리를 담당하는 URL 패턴.
    path('<int:question_id>/update/', views.QuestionUpdateView.as_view(), name='update'),

    # 질문 삭제(설문 삭제) 페이지 이동 및 데이터베이스 처리를 담당하는 URL 패턴.
    path('<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='delete'),
]
