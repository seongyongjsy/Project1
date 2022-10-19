from asyncore import write
from django.db import models
from django.utils import timezone


class Board(models.Model):
    number = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=10)
    content = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)
    count = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.writer}이(가) 작성한 {self.number} 게시글"

    def getInfo(self):
        return f"{self.number} - {self.title} - {self.writer}"
            