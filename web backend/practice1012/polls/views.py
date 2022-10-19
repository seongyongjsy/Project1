from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import QuestionForm

from .models import Question, Answer

from datetime import datetime


def list(request):
    """설문 목록 페이지로 이동하는 뷰 함수."""


    context = {
        'question_list': Question.objects.filter(date__lte=timezone.now())
    }

    return render(request, "polls/list.html", context)


class QuestionListView(ListView):
    """설문 목록 페이지로 이동하는 뷰 클래스."""    ##### model, queryset, get_queryset() 중 하나는 반드시 작성해야 함. #####

    def get_queryset(self):
        return Question.objects.filter(date__lte=timezone.now())
    template_name = "polls/list.html"

    context_object_name = "question_list"


def detail(request, question_id):
    """설문 상세 페이지로 이동하는 뷰 함수."""

    context = {
        'question': get_object_or_404(Question, pk=question_id)
    }

    return render(request, "polls/detail.html", context)


class QuestionDetailView(DetailView):
    """설문 상세 페이지로 이동하는 뷰 클래스."""

    def get_queryset(self):
        return Question.objects.filter(date__lte=timezone.now())

    template_name = 'polls/detail.html'

    context_object_name = 'question'

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

    form_class= QuestionForm

    template_name = 'polls/create_form.html'
    success_url = reverse_lazy('polls:list')
    
    def form_valid(self, form):
        # form: ModelForm 클래스. 여기서는 QuestionForm 객체.
        # form.instance: 모델 클래스. 여기서는 Question 객체.
        # form.data: 양식 데이터와 관련된 모든 데이터를 담은 사전 객체. 일반적으로 사용 안함.
        # form.cleaned_data: 양식 데이터를 담은 사전 객체. 일반적으로 사용
        print('memo:', form.cleaned_data['memo'])

        return super().form_valid(form) # success_url에 설정된 URL로 리다이렉트.
        #return redirect(reverse_lazy('polls:list')) # 지정된 URL로 리다이렉트

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
