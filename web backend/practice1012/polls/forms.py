from django import forms

from .models import Question, Answer


class QuestionForm(forms.Modelform):
    """질문 모델과 양식 데이터를 관리하기 위한 사용자 정의 모델 폼 클래스."""

    memo = forms.CharField(max_length=10)
    # file = forms.FileField()

    class Meta:
        """이 모델 폼 클래스에서 다룰 데이터 설정."""

        model = Question  # 폼과 연결할 모델 클래스.
        fields = ['text', 'date']   # 폼에서 다룰 모델의 필드들.
        widgets = {
        #   'text': forms.TextInput()   # input 태그로 표현.
            'text': forms.Textarea(attrs={'style': 'resize:none; width:180px; height:80px;'}),  # textarea 태그로 표현.
            'date': forms.DateTimeInput(),  # input 태그로 표현.
            'memo': forms.TextInput()
            # 'file': forms.FileInput(),

        }