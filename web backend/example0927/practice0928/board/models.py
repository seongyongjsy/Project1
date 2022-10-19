from datetime import datetime
from unittest.util import _MAX_LENGTH

from django.db import models

# Create your models here.
class Board(models.Model):
    """게시글 테이블을 나타내는 모델 클래스.""" 
    
    num = models.IntegerField(primary_key=True)   # 게시글 번호.
    title = models.CharField(max_length=50, null=False )    # 게시글 제목.
    writer = models.CharField(max_length=20, null=False)   # 게시글 작성자.
    content = models.CharField()  # 게시글 내용.
    date = models.DateTimeField(default=datetime.now())     # 게시글 작성일.


    def __str__(self) -> str:
        return f"{self.num}\t{self.title}\t{self.writer}"

        
# class Reply(models.Model):
    # """댓글 테이블을 나타내는 모델 클래스."""