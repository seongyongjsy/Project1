from django.db import models
from django.utils import timezone

from datetime import timedelta


class Question(models.Model):
    """설문 조사에서 질문을 담당하는 클래스."""
    text = models.TextField(max_length=3000) # 질문 내용.
    date = models.DateTimeField(default=timezone.now)  # 게시일.

    def was_published_recently(self) -> bool:
        """최근에 게시된 질문인지 검사하는 함수."""
        return self.date > timezone.now() - timedelta(days=1)

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

