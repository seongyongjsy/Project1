from django.urls import path

from . import views


app_name = 'board'
urlpatterns = [
    # 게시판 페이지로 이동하는 URL 패턴.
    path('list/', views.BoardListView.as_view(), name='list' ),

    # 게시글 상세 페이지로 이동하는 URL 패턴.
    path('<int:pk>/', views.BoardDetailView.as_view(), name='detail'),

    # 글쓰기 페이지로 이동하거나 게시글 데이터 생성 처리를 하는 URL 패턴.
    path('write/', views.BoardCreateView.as_view(), name='create'),

    # 댓글 작성 처리를 하는 URL 패턴.
    path('<int:pk>/reply/write/', views.reply_create, name='reply_create'),
]