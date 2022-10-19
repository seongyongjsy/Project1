from django.shortcuts import render

from .models import Board

# Create your views here.
def board_list(request):
    """게시글 목록 페이지로 이동하는 뷰 함수."""
    
    # 데이터베이스에서 모든 게시글 데이터를 가져옴.
    board_list = Board.objects.all()
    print(board_list)

    return render(request, "board/list.html", {'board_list': board_list})


def board_write(request): 
    """게시글 작성 페이지로 이동하는 뷰 함수."""
    
    if request.POST:
        # POST 방식으로 요청한 경우, 전달받은 새 게시글 데이터를 데이터베이스에 저장.
       
        # for key in request.POST.keys():
        #     print(f"{key=}, value={request.POST[key]}")
        
        # HTML로부터 전달받은 데이터를 POST 객체에서 꺼내서 데이터베이스에 입력하는 코드.
        Board.objects.create(
            num = 1000,
            title = request.POST['title'],
            writer = request.POST['writer'],
            content = request.POST['content'],
        )

        # 데이터베이스에 데이터를 입력한 후 게시글 목록 페이지로 이동.
        return render(request, "board/write.html")
    else:
        # GET 방식으로 요청한 경우, 게시글 작성 페이지로 이동.
        return render(request, "board/write.html")

