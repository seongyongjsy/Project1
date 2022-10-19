from xmlrpc.client import boolean
from django.db import models


from django.utils import timezone

from datetime import timedelta


class Question(models.Model):
    """설문 조사에서 질문을 담당하는 클래스."""
    text = models.TextField(max_length=3000)  # 질문 내용.
    date = models.DateTimeField(default=timezone.now)  # 게시일.

    # 관리자 페이지에서 이 메소드를 출력할 때 적용할 세부 설정을 추가하는 데코레이터
    @admin.display(
        boolean=True,   # 함수 실행 결과 True, False 값을 관리자 페이지에서 아이콘으로 표시할지 여부
        ordering='-date',   # 열 이름을 클릭했을 때 정렬 기준.
        description='최근 24시간 이내에 게시된 질문인지 여부', # 열 이름에 표시할 문자열.
    )

    def was_published_recently(self) -> bool:
        """최근에 게시된 질문인지 검사하는 함수."""
        # return self.date > timezone.now() - timedelta(days=1)
        return timezone.now() - timedelta(days=1) < self.date < timezone.now()

    # 관리자 페이지에서 확인하기 위해 메소드를 재정의.
    def __str__(self) -> str:
        return f"{self.text}"


class Answer(models.Model):
    """설문 조사에서 답변을 담당하는 클래스."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 원본 질문.
    text = models.TextField(max_length=1000)  # 답변 내용.
    count = models.BigIntegerField(default=0)  # 투표 수.

    # 관리자 페이지에서 확인하기 위해 메소드를 재정의.
    def __str__(self) -> str:
        return f"{self.text}"
