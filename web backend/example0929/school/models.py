"""school 앱에서 사용하는 모델을 작성하는 파일."""


from django.db import models

from datetime import datetime


class Student(models.Model):
    """학생을 나타내는 모델 클래스."""

    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)  # 학생의 이름.
    grade = models.IntegerField()  # 학년.
    st_class = models.IntegerField()  # 반.

    def __str__(self) -> str:
        return f"{self.grade}학년 {self.st_class}반 {self.name}"


class Exam(models.Model):
    """시험을 나타내는 모델 클래스."""

    # id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)  # 시험 제목.
    subject = models.CharField(max_length=10)  # 시험 과목.
    date = models.DateTimeField(default=datetime.now())  # 시험 날짜.

    def __str__(self) -> str:
        return f"{self.subject} {self.title}"


class Score(models.Model):
    """시험 점수를 나타내는 모델 클래스."""

    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # 시험을 응시한 학생의 ID.
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)  # 학생이 응시한 시험의 ID.
    score = models.FloatField(default=0.0)  # 시험 점수.

    def __str__(self) -> str:
        return f"응시자: {self.student} / 시험: {self.exam} / 점수: {self.score}"
