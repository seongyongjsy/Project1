from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import  redirect

from .models import Board, Reply


class BoardListView(generic.ListView):
    """내장 뷰 클래스인 ListView 클래스를 상속하여 구현한 사용자 정의 뷰 클래스."""
    
    paginate_by = 10

    # ListView는 model, queryset, get_queryset() 중 하나를 반드시 작성해야 한다.
    def get_queryset(self):
        # HttpRequest 객체를 통해 전달받은 검색기준 및 검색어를 변수에 저장.
        search_type = self.request.GET.get('searchType', '')
        search_word = self.request.GET.get('searchWord', '')
    
        result = None   # 응답할 게시글 데이터를 저장할 변수 선언.  
        if search_type and search_word:  # 검색기준 및 검색어를 전달받은 경우,
            match search_type:
                case 'title':   # 검색기준이 제목인 경우,
                # 제목에 검색어가 포함되는 게시글 선택
                    result = Board.objects.filter(title__contains=search_word)  
                case 'content':  # 검색기준이 내용인 경우,
                # 내용에 검색어가 포함되는 게시글 선택
                    result = Board.objects.filter(content__contains=search_word)  
                case'writer':   # 검색기준이 작성자인 경우,
                # 작성자의 사용자 이름에 검색어가 포함되는 게시글 선택.
                    result = Board.objects.filter(writer__username__contains=search_word)
        else:   # 검색기준 또는 검색어를 전달받지 못한 경우,
        # 모든 게시글 데이터를 선택
            result = Board.objects.all()

        # 데이터베이스에서 가져온 게시글 데이터를 반환해서 템플릿에 전달.
        return result.order_by('-date')

    def get_context_data(self, **kwargs):
        # 요총을 통해 전달받은 검색기준 및 검색어를 다시 템플릿으로 전달한다.
        context = super().get_context_data(**kwargs)
        search_type = self.request.GET.get('searchType', '')
        search_word = self.request.GET.get('searchWord', '')
        if search_type and search_word:
            context['searchType'] = search_type
            context['searchWord'] = search_word
        return context


class BoardDetailView(generic.DetailView):
    """내장 뷰 클래스인 DetailView 클래스를 상속받아 구현한 사용자 정의 클래스 뷰."""
    
    model = Board
    fiedls = [ 'title', 'content']

    # LoginRequiredMixin클래스
    # 클래스 기반 뷰에 추가해서 로그인 여부 검사 기능을 추가하는 보조 클래스.
    # 상속할 때 반드시 가장 왼쪽에 작성해야 한다.
    # 이 클래스를 추가한 경우, login_url 클래스 변수를 작성해야 한다.
    # login_url: 로그인 하지 않은 경우 이동할 URL.
    login_url = reverse_lazy('user:login')

    def get_queryset(self):
        # 전달받은 pk(=board_id)를 변수에 저장.
        pk = self.kwargs.get('pk')

        # 데이터베이스에서 조회하고자 하는 게시글 데이터를 가져옴.
        board = Board.objects.get(pk=pk)

        # 기존의 조회수를 1 증가시킴.
        board.count += 1

        # 변경한 내용을 데이터베이스에 반영.
        board.save()
        
        # 게시글 데이터를 QuerySet 객체 형태로 반환해서 템플릿으로 전달.
        return Board.objects.filter(pk=pk)

class BoardCreateView(generic.CreateView):
    """내장 뷰 클래스인 CreateView 클래스를 상속받아 구현한 사용자 정의 클래스 뷰."""
    
    model = Board
    fields = ['title', 'content']
    

    def form_vaild(self, form):
        # 전달받은 양식 데이터를 데이터베이스에 저장하기 전,
        # 현재 접속한 사용자 데이터를 모델 데이터에 입력.
        form.instance.writer = self.request.user

        # 설정된 모델 데이터를 데이터베이스에 저장.
        form.save()

        # 글쓰기 완료 후 게시판 페이지로 리다이렉트.
        return redirect(reverse_lazy('board:list'))

@login_required(login_url=reverse_lazy('user:login'), redirect_field_name='/board/list/')
def reply_create(request, board_id):
    """댓글 작성 처리를 하는 뷰 함수."""
    # 템플릿에서 form 태그를 통해 전달받은 댓글 내용을 변수에 저장.
    content = request.POST.get('content', '')
    # HttpRequest 객체에 저장된 로그인한 사용자 정보를 변수에 저장.
    user = request.user

    # 데이터베이스에 댓글 데이터 생성.
    Reply.objects.create(content=content, writer=user, board_id=board_id)
    # Board.objects.get(pk=board_id).reply_set.create(content=content, writer=user)
    
    # 댓글 작성 페이지로 리다이렉트.
    return redirect(reverse('board:detail', kwargs={'pk':board_id}))

