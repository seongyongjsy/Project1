from datetime import datetime
from django.shortcuts import render

from .models import Board


def home(request):
    return render(request, "home.html")


def summary(request):
    board = Board()
    board.title = '테스트 제목'
    board.writer = '홍길동'
    
    # 콘텍스트: 템플릿으로 전달할 데이터를 부르는 표현. 키-값 쌍의 사전 형태로 작성함.
    context = {
        'a': 10,
        'b': 20,
        'student': {
            'name': '홍길동',
            'age' : 20,
            'major': '컴퓨터공학',
        },
        'board': board,
        'today': datetime.now(),
    }
    return render(request, "summary.html", context)


def board_list(request):
    return render(request, "board/list.html")


def board_detail(request, board_num):
    board_num = request.GET['board_num']
    print("템플릿에서 전달받은 게시글 번호:", board_num)
    
    return render(request, "board/detail.html")
