from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from datetime import timedelta

from .models import Question


class QuestionTestCase(TestCase):
    """질문 모델에 대한 자동화 테스트 케이스를 작성하는 클래스."""

    def test_was_published_recently_with_future_question(self):
        """미래에 게시 예정인 질문에 대해서, was_published_recently 메소드가 False를 반환하는지 검사하는 테스트 케이스."""
        
        # 미래의 날짜 설정.
        time = timezone.now() + timedelta(days=30)

        # 게시일로 미래의 날짜를 가지는 테스트용 질문 데이터 생성.
        future_question = Question(date=time)

        # 검증 실행.
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """오래된 질문에 대해서, was_published_recently 메소드가 False를 반환하는지 검사하는 메소드."""

        # 과거 날짜-시간 설정.
        time = timezone.now() - timedelta(days=1, seconds=1)

        # 게시일이 과거인 테스트용 질문 데이터 생성.
        old_question = Question(date=time)

        # 검증 실행.
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """최근 게시된 질문에 대해서, was_published_recently() 메소드가 정상 동작하는지 테스트하는 메소드."""
        
        # 최근 날짜-시간 설정.
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)

        # 해당 날짜-시간의 게시일을 갖는 질문 데이터 생성.
        recent_question = Question(date=time)

        # 검증 실행 - 최근 게시된 질문의 해당 메소드가 True를 반환하는지 검사.
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionViewTestCase(TestCase):
    """설문 앱의 뷰에 대한 자동화 테스트 케이스를 작성하는 클래스."""
    
    def test_no_question_at_list_page(self):
        """설문 목록 페이지에 접속했을 때, 질문 데이터가 없는 경우를 검사하는 메소드."""
        
        # 설문 목록 페이지의 URL을 구해서 접속 시도.
        response = self.client.get(reverse('polls:list'))

        # 페이지 접속 결과, Http 상태 응답 코드가 200(=정상 접속)인지 검사.
        self.assertEqual(response.status_code, 200)

        # 페이지 접속 결과, 웹 페이지에 안내 메시지가 포함되어 있는지 검사.
        self.assertContains(response, "등록된 설문이 없습니다.")

        # 페이지 접속 결과, 콘텍스트가 비어있는지 검사.
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_past_questions_at_list_page(self):
        """설문 목록 페이지에 접속했을 때, 과거 질문 데이터가 등록된 경우를 검사하는 메소드."""

        # 테스트용 데이터베이스에 과거 질문 데이터 입력.
        q = Question.objects.create(text='test1', date=timezone.now()-timedelta(days=30))

        # 설문 목록 페이지의 URL을 구해서 접속 시도.
        response = self.client.get(reverse('polls:list'))

        # 페이지 접속 결과, Http 상태 응답 코드가 200(=정상 접속)인지 검사.
        self.assertEqual(response.status_code, 200)

        # 페이지 접속 결과, 콘텍스트가 일치하는지 검사.
        self.assertQuerysetEqual(response.context['question_list'], [q])

    def test_future_questions_at_list_page(self):
        """설문 목록 페이지에 접속했을 때, 미래 질문 데이터가 등록된 경우를 검사하는 메소드."""

        # 테스트용 데이터베이스에 미래 질문 데이터 입력.
        Question.objects.create(text='test', date=timezone.now()+timedelta(days=30))

        # 설문 목록 페이지의 URL을 구해서 접속 시도.
        response = self.client.get(reverse('polls:list'))

        # 페이지 접속 결과, Http 상태 응답 코드가 200(=정상 접속)인지 검사.
        self.assertEqual(response.status_code, 200)

        # 페이지 접속 결과, 웹 페이지에 안내 메시지가 포함되어 있는지 검사.
        self.assertContains(response, "등록된 설문이 없습니다.")

        # 페이지 접속 결과, 콘텍스트가 비어있는지 검사.
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_past_future_questions_at_list_page(self):
        """설문 목록 페이지에 접속했을 때, 과거 및 미래 질문 데이터가 등록된 경우를 검사하는 메소드."""

        # 테스트용 데이터베이스에 과거 및 미래 질문 데이터 입력.
        q1 = Question.objects.create(text='test1', date=timezone.now()-timedelta(days=30))
        q2 = Question.objects.create(text='test2', date=timezone.now()+timedelta(days=30))

        # 설문 목록 페이지의 URL을 구해서 접속 시도.
        response = self.client.get(reverse('polls:list'))

        # 페이지 접속 결과, Http 상태 응답 코드가 200(=정상 접속)인지 검사.
        self.assertEqual(response.status_code, 200)

        # 페이지 접속 결과, 콘텍스트가 일치하는지 검사.
        self.assertQuerysetEqual(response.context['question_list'], [q1])

    def test_no_question_at_detail_page(self):
        """설문 상세 페이지에 접속할 때, 질문이 없는 경우를 테스트하는 케이스."""

        # 접속을 시도할 질문의 ID를 저장.
        question_id = 1

        # 질문 ID가 1인 설문 상세 페이지 접속 시도.
        response = self.client.get(reverse('polls:detail', args=(question_id,)))

        # 페이지 접속 결과, Http 상태 응답 코드가 404(Page Not Found)인지 검사.
        self.assertEqual(response.status_code, 404)
    
    def test_question_at_detail_page(self):
        """설문 상세 페이지에 접속할 때, 질문이 있는 경우를 테스트하는 케이스."""

        # 테스트용 데이터베이스에 질문 데이터 생성.
        question = Question.objects.create(text='테스트용 질문 텍스트입니다.', date=timezone.now())

        # 접속을 시도할 질문의 ID를 저장.
        question_id = question.id

        # 질문 ID가 1인 설문 상세 페이지 접속 시도.
        response = self.client.get(reverse('polls:detail', args=(question_id,)))

        # 페이지 접속 결과, Http 상태 응답 코드가 200(정상 접속)인지 검사.
        self.assertEqual(response.status_code, 200)

        # 페이지 접속 결과, 질문 텍스트가 페이지에 포함되어 있는지 검사.
        self.assertContains(response, question.text)
