from django.contrib import admin

from .models import Question, Answer


# 관리자 페이지에서 모델 데이터를 관리할 수 있도록 등록.
admin.site.register([Question, Answer])
