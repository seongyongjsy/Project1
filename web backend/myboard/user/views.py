from django.contrib.auth import models, forms
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


class UserCreateView(generic.CreateView):
    """
    내장 뷰 클래스인 CreateView를 상속하여 구현한 사용자 정의 CreateView.
    GET 요청 시 회원가입 페이지로 이동하고,
    POST 요청 시 내장 모델 클래스인 User를 사용하여 회원가입 처리를 한다. 
    """

    # CreateView는 어떤 모델, 필드를 다룰지 설정해야 한다.

    # 1. model, fields 변수를 통해 직접 설정하는 경우.
    # model = models.User
    # fields = ['username', 'password', 'email', 'first_name', 'last_name']

    # 1-2. 내장 모델 클래스를 수정해서 사용하는 경우.
    # from . models import CustomUser
    # model: CustomUser
    # fields = ['username', 'password', 'password2', 'address']
    
    # 2. form_class 변수를 통해 일괄 설정하는 경우.
    form_class = forms.UserCreationForm

    # 2-2. 내장 폼 클래스를 수정해서 사용하는 경우.
    # from . forms import CustomUserCreationForm
    # form_class = CustomUserCreationForm

    template_name = 'user/user_form.html'  # GET 요청을 처리할 때 응답할 템플릿 파일.
    success_url = reverse_lazy('user:login')    #  POST 요청을 처리할 때 리다이렉트할 URL.


