from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Question, Answer

from datetime import datetime


def list(request):
    """설문 목록 페이지로 이동하는 뷰 함수."""

    # 데이터베이스에서 모든 질문 데이터들을 가져와서 콘텍스트로 구성.
    # get_list_or_404(): 데이터베이스에서 데이터 여러 건을 조회하되, 존재하지 않으면 404 상태 응답 코드로 처리.
    context = {
        # 'question_list': get_list_or_404(Question, date__lte=timezone.now())
        'question_list': Question.objects.filter(date__lte=timezone.now())
    }

    # 콘텍스트를 템플릿에 전달.
    return render(request, "polls/list.html", context)


class QuestionListView(ListView):
    """설문 목록 페이지로 이동하는 뷰 클래스."""

    ##### model, queryset, get_queryset() 중 하나는 반드시 작성해야 함. #####

    # model 클래스 변수.
    # 데이터베이스에서 가져와서 이 뷰에서 처리할 데이터 모델.
    # 지정된 모델과 연결된 테이블에서 '모든 데이터'를 가져와서 처리한다.
    # model = Question

    # queryset 클래스 변수.
    # 데이터베이스에서 가져올 데이터 목록.
    # model보다 복잡한 조건을 적용할 수 있음.
    # queryset = Question.objects.filter(date__lte=timezone.now())

    # get_queryset() 메소드.
    # 데이터베이스에서 가져올 데이터를 반환하는 메소드.
    # queryset보다 복잡한 코드를 설정할 수 있음.
    def get_queryset(self):
        return Question.objects.filter(date__lte=timezone.now())

    # template_name 클래스 변수.
    # 뷰에서 응답할 템플릿 파일 이름.
    # 기본 설정은 <앱 이름>/<lower(모델 이름)>_list.html
    template_name = "polls/list.html"

    # context_object_name 클래스 변수.
    # 템플릿으로 전달할 목록 데이터의 이름.
    # 기본 설정은 object_list 또는 <lower(모델 이름)>_list
    context_object_name = "question_list"


def detail(request, question_id):
    """설문 상세 페이지로 이동하는 뷰 함수."""

    # 전달받은 질문 ID 값을 이용해서 데이터베이스에서 해당 질문 데이터를 가져오고 콘텍스트로 구성.
    # get_object_or_404(): 데이터베이스에서 데이터 1건을 조회하되, 존재하지 않으면 404 상태 응답 코드로 처리.
    context = {
        'question': get_object_or_404(Question, pk=question_id)
    }

    # 콘텍스트를 템플릿에 전달.
    return render(request, "polls/detail.html", context)


class QuestionDetailView(DetailView):
    """설문 상세 페이지로 이동하는 뷰 클래스."""

    # ListView와 마찬가지로, model, queryset, get_queryset() 중 하나를 반드시 작성해야 한다.
    # 이 때, queryset과 get_queryset()의 경우, 전달된 pk값을 이용해서 먼저 데이터를 선택한 후 필터링을 나중에 적용한다.
    # model = Question
    # queryset = Question.objects.filter(date__lte=timezone.now())
    def get_queryset(self):
        return Question.objects.filter(date__lte=timezone.now())

    # ListView와 마찬가지로, 응답할 템플릿 파일 이름을 지정할 수도 있다.
    # 기본 설정은 '<앱 이름>/<lower(모델 이름)>_detail.html'
    template_name = 'polls/detail.html'

    # ListView와 마찬가지로, 콘텍스트 객체의 이름을 지정할 수도 있다.
    # 기본 설정은 'object' 또는 '<lower(모델 이름)>'
    context_object_name = 'question'

    # pk_url_kwarg 클래스 변수.
    # 데이터베이스에서 특정 데이터 1건을 조회하기 위해,
    # URL에 추가해서 보내준 PK 데이터를 지정하는 변수 이름.
    # 기본 설정은 'pk'.
    pk_url_kwarg = 'question_id'


def choice(request, question_id):
    """질문에 대한 답변을 처리하고 설문 결과 페이지로 이동하는 뷰 함수."""

    try:
        # 사용자가 선택한 답변의 ID를 이용해서 데이터베이스에서 일치하는 답변 데이터를 가져오고,
        # 해당 데이터의 투표 수를 1 증가시킨 후 저장.
        answer_id = request.POST['answer_id']
        # answer = Answer.objects.get(pk=answer_id)
        answer = Question.objects.get(pk=question_id).answer_set.filter(pk=answer_id)[0]
        answer.count += 1
        answer.save()
    except:
        pass

    # 설문 결과 페이지로 리다이렉트.
    return redirect(f"/polls/{question_id}/result/")


def result(request, question_id):
    """설문 결과 페이지로 이동하는 뷰 함수."""

    # 설문 결과 페이지에서 확인하기 위해, 현재 답변 중인 질문에 대한 모든 답변 데이터를 가져와서 콘텍스트로 구성.
    context = {
        # 'answer_list': Answer.objects.filter(question_id=question_id)
        'answer_list': Question.objects.get(pk=question_id).answer_set.all()
    }

    # 콘텍스트를 템플릿에 전달.
    return render(request, 'polls/result.html', context)


class QuestionCreateView(CreateView):
    """질문 생성(설문 등록) 페이지로 이동하거나 데이터베이스에 처리하는 뷰 클래스."""

    # 이 뷰에서 처리할 모델 클래스.
    model = Question
    # 템플릿에서 입력받을 필드 이름 목록.
    fields = ['text', 'date']
    
    # 기본 값: '<앱 이름>/<lower(모델 이름)>_form.html'
    template_name = 'polls/create_form.html'

    # success_url 클래스 변수.
    # 데이터베이스에 데이터를 생성한 후, 리다이렉트 할 URL을 설정하는 변수.
    # URL 패턴 이름으로 지정할 때, reverse() 함수 대신 reverse_lazy() 함수를 사용해야 함.
    # success_url = reverse_lazy('polls:list')

    # get_success_url() 메소드.
    # 데이터베이스에 데이터를 생성한 후, 리다이렉트 할 URL을 설정하는 함수.
    def get_success_url(self):
        return reverse_lazy('polls:list')

    def post(self, request, *arg, **kwargs):
        text = request.POST['text']
        date = request.POST['date']
        date = datetime.strptime(date, '%Y-%m-%d')
        if date < datetime.now():
            date = datetime.now()
        Question.objects.create(text=text, date=date)
        return HttpResponseRedirect(reverse_lazy('polls:list'))


class QuestionUpdateView(UpdateView):
    """질문 수정(설문 변경) 페이지로 이동시키거나 데이터베이스 처리를 하는 뷰 클래스."""

    model = Question
    fields = ['text', 'date']
    success_url = reverse_lazy('polls:list')

    pk_url_kwarg = 'question_id'  # 기본 값: 'pk'
    template_name = 'polls/update_form.html'  # 기본 값: '<앱 이름>/<lower(모델 이름)>_form.html'
    # context_object_name = 'q'  # 기본 값: 'object' 또는 '<lower(모델 이름)>'


class QuestionDeleteView(DeleteView):
    """질문 삭제(설문 삭제) 페이지로 이동시키거나 데이터베이스 처리를 하는 뷰 클래스."""

    model = Question
    success_url = reverse_lazy('polls:list')
