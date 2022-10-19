from django.shortcuts import render, redirect,  get_object_or_404, get_list_or_404

from .models import Question, Answer


def list(request):
    """설문 목록으로 이동하는 뷰 함수."""

    # 데이터베이스에서 모든 질문 데이터들을 가져와서 콘텍스트로 구성.
    # get_list_or_404(): 데이터베이스에서 데이터 여러 건을 조회하되, 존재하지 않으면 404 상태 응답 코드로 처리
    context = {
        'question_list': get_list_or_404(Question)
    }

    # 콘텍스트를 템플릿에 전달.
    return render(request, "polls/list.html", context)


def detail(request, question_id):
    """설문 상세 페이지로 이동하는 뷰 함수."""

    # 전달받은 질문 ID 값을 이용해서 데이터베이스에서 해당 질문 데이터를 가져오고 콘텍스트로 구성.
    # get_object_or_404(): 데이터베이스에서 데이터 1건을 조회하되, 존재하지 않으면 404 상태 응답 코드로 처리
    context = {
        'question': get_object_or_404(Question, pk=question_id)
    }

    # 콘텍스트를 템플릿에 전달.
    return render(request, "polls/detail.html", context)


def choice(request):
    """질문에 대한 답변을 처리하고 설문 결과 페이지로 이동하는 뷰 함수."""
    
    # 사용자가 선택한 답변의 ID를 이용해서 데이터베이스에서 일치하는 답변 데이터를 가져오고,
    # 해당 데이터의 투표 수를 1 증가시킨 후 저장.
    ############################################
    try:
        answer_id = request.POST['answer_id']
        # answer = Answer.objects.get(pk=answer_id])
        answer = Question.objects.get(pk=question_id).answer_set.filter(pk=answer_id)[0]
        answer.count += 1
        answer.save()
    except:
        pass
    
    
    # 설문 결과 페이지로 리다이렉트.   
    return redirect(f"/polls/{question_id}/result/")


    # 설문 결과 페이지에서 확인하기 위해 현재 답변 중인 질문에 대한 모든 답변 데이터를 가져와서 콘텍스트로 구성.
    context = {
        # 'answer_list': Answer.objects.filter(question_id=question_id)
        'answer_list': Question.objects.get(pk=question_id).answer_set.all()
    }

    # 콘텍스트를 템플릿에 전달.
    return render(request, 'polls/result.html', context) 