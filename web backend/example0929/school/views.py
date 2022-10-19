"""school 앱에서 사용하는 뷰 스크립트 파일."""


from django.shortcuts import render, redirect

# 이 파일이 위치한 폴더(school) 내 models 모듈에서 Student, Exam 모델 클래스를 불러옴.
from .models import Student, Exam, Score


def home(request):
    """홈 화면으로 이동하는 뷰 함수."""
    return render(request, "school/home.html")


def student_list(request):
    """학생 명단 페이지로 이동하는 뷰 함수."""

    # 데이터베이스에서 모든 학생 데이터를 가져옴.
    context = {
        'student_list': Student.objects.all()
    }

    return render(request, "school/student/list.html", context)


def exam_list(request):
    """시험 점수 페이지로 이동하는 뷰 함수."""

    # 데이터베이스에서 모든 시험 데이터를 가져옴.
    context = {
        'exam_list': Exam.objects.all()
    }

    return render(request, "school/exam/list.html", context)


def exam_detail(request):
    """특정 시험에 응시한 학생들의 점수를 확인하는 페이지로 이동하는 뷰 함수."""

    # 웹 페이지로부터 전달받은 시험 ID 출력.
    exam_id = request.GET['exam_id']
    # print("조회할 시험의 ID:", exam_id)

    # 데이터베이스에서 특정 시험 데이터 및 해당 시험 점수 데이터를 가져옴.
    context = {
        'exam': Exam.objects.get(id=exam_id),
        # 'score_list': Score.objects.filter(exam_id=exam_id),
    }

    return render(request, "school/exam/detail.html", context)


def score_insert(request):
    """점수 입력 페이지로 이동하는 함수."""

    if request.POST:
        # POST 방식으로 통신하는 경우,
        # 전달받은 점수 데이터를 데이터베이스에 입력.
        exam_id = request.POST['exam_id']
        student_id = request.POST['student_id']
        score = request.POST['score']
        Score.objects.create(student_id=student_id, exam_id=exam_id, score=score)
        # return render(request, "school/exam/detail.html")
        return redirect(f"/school/exam/detail/?exam_id={exam_id}")
    else:
        # GET 방식으로 통신하는 경우,
        # 시험 상세 페이지로부터 전달받은 시험 ID 데이터를 다시 점수 입력 페이지로 전달.
        context = {
            'exam_id': request.GET['exam_id']
        }
        return render(request, "school/score/insert.html", context)

