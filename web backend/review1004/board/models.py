from django.utils import timezone
from django.db import models

from datetime import datetime
from textwrap import shorten


class Board(models.Model):
    # id = models.BigAutoField()
    num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=20)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f"{self.num} - {shorten(self.title, 10, placeholder='...')} - {self.writer}"


class Reply(models.Model):
    # id = models.BigAutoField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    writer = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)

    # shell에서 이 모델 객체를 출력할 때 사용하는 특수 메소드.
    def __repr__(self) -> str:
        return f"""
        {{
            {'id':8}: {self.id},
            {'board_id':8}: {self.board_id},
            {'content':8}: {shorten(self.content, 10)},
            {'writer':8}: {self.writer},
            {'date':8}: {self.date:%Y-%m-%d %H:%M:%S}
        }}"""

    # 관리자 페이지에서 이 모델 객체를 출력할 때 사용하는 특수 메소드.
    # 또는, __repr__ 함수가 재정의되어 있지 않으면 shell에서도 이 메소드를 사용한다.
    def __str__(self) -> str:
        return f"{self.writer}이(가) {self.board.num}번 게시글에 작성한 댓글."
