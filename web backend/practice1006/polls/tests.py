from django.test import TestCase
from django.utils import timezone

from datetime import timedelta

from . models import Question


class QustionTestCase(TestCase):
    """질문 모델에 대한 테스트 케이스를 작성하는 클래스."""

    def test_was_published_recently(self):
        """미래에 게시 예정인 질문에 대해서,
        was_published_recently 메소드가 False를 반환하는지 검사하는 테스트 케이스."""
        time = timezone.now() + timedelta(days=30)  # 미래의 날짜 설정.
        future_question = Question(date=time)   # 게시일로 미래의 날짜를 가지는 테스트용 질문 데이터 생성. 
        self.assertIs(future_question.was_published_recently(),False)   # 검증 실행. 
        