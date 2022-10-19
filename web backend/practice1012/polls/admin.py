from django.contrib import admin

from .models import Question, Answer


# 관리자 페이지에서 모델 데이터를 관리할 수 있도록 등록.
# admin.site.register([Question, Answer])
# admin.site.register(Question)
# admin.site.register(Answer)


class AnswerInline(admin.StackedInline):
    """질문 데이터를 생성/수정할 때 답변 데이터도 같이 생성/수정할 수 있도록 설정하는 인라인 클래스."""
    
    model = Answer  # 인라인 방식으로 관리할 FP 모델 클래스를 설정하는 옵션. 여기서는 답변 모델 클래스를 지정.
    extra = 3   # 관리자 페이지에서 몇 개의 항목을 보여줄 것인지 설정하는 옵션. 
    exclude = ['count']  # 출력하고 싶지 않은 모델의 필드를 설정하는 옵션.


class QuestionModelAdmin(admin.ModelAdmin):
    """질문 모델을 좀 더 상세하게 관리하기 위한 사용자 정의 모델 관리자 클래스."""
    

    # fields 클래스 변수.
    # 모델 데이터를 추가할 때 입력받을 필드 목록.
    # 설정하지 않으면 모델에 작성된 모든 필드를 관리하도록 설정한다.
    # fields = ['text', 'date']

    # fieldsets 클래스 변수.
    # fields 클래스 변수를 대체해서 모델 데이터를 조작할 때 좀 더 상세하게 표현하기 위한 설정.
    # 여러 개의 필드셋(=여러 개의 필드를 묶은 그룹)을 만들어서 설명을 추가하는 등 다양한 기능을 제공한다.
    fieldsets = (
        # 첫 번째 필드셋 설정.
        ('질문 내용', { # 필드셋의 제목.
            'fields':('text',), # 이 필드셋에서 다룰 모델의 필드들.
        }),
        # 두 번째 필드셋 설정.
        ('게시일',{ # 필드셋의 제목
            'fields': ('date',),    # 이 필드셋에서 다룰 모델의 필드들
            'classes': ('collapse'),    # 기본적으로 이 필드셋을 감추기 설정.
            'description': '미래 날짜-시간으로 설정할 경우, 예약 게시글로 설정합니다.'  # 이 필드셋에 대한 상세 설명.
        }),
    )

    # list_display: 질문 목록에서 출력할 열 설정. 모델에 작성한 필드 또는 메소드 이름을 지정할 수 있다.
    list_display = ['text', 'date', 'was_published_recently']
    # list_filter: 질문 목록에서 필터를 적용할 열 설정. 모델에 작성한 필드 또는 메소드 이름을 지정할 수 있다.
    list_filter = ['date']
    # search_fields: 검색 대상 필드 이름 목록.
    search_fields = ['text']

    # inlines: 질문 모델 데이터를 생성/수정할 때 함께 수정할 모델 데이터에 대한 인라인 클래스.
    inlines = [AnswerInline]

# 관리자 기능에 질문 모델 및 질문 모델을 관리하기 위한 모델 관리자 클래스를 함께 등록.
admin.site.register(Question, QuestionModelAdmin)
