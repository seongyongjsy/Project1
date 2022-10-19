# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def board_list(request):
    """board/list 요청 URL을 처리하여 게시글 목록 페이지로 접속시키는 뷰 함수."""
    return HttpResponse("게시글 목록 페이지 접속.")

def board_detail(request, board_num):
    """board/<int:board_num> 요청 URL을 처리하여 게시글 상세 페이지로 접속시키는 뷰 함수."""
    print("URL을 통해 전달받은 게시글 번호:", board_num)
    return HttpResponse("게시글 상세 페이지 접속.")
