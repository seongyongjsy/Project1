"""
practice0928 프로젝트에 대한 장고 설정 파일.

장고 4.1.1 버전에서 'django-admin startproject' 명령어를 통해 생성되었다.

이 파일에 대한 추가 정보 링크.
https://docs.djangoproject.com/en/4.1/topics/settings/

이 파일에 대한 모든 설정 값 레퍼런스 문서 링크.
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


##################################################


# 프로젝트 경로(Build path)를 저장하는 옵션. 설정된 경로는 아래와 같다.
# C:\Workspace\web-backend\practice0928\
# 주로 다른 옵션에서 사용되는 경로이다.
# 설정된 경로는 Path 객체로써, / 연산자를 통해 경로를 추가할 수 있다.
# ex) BASE_DIR / 'subdir'
# ex) BASE_DIR / 'db.sqlite3'
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


##################################################


# 빠른 개발을 위한 설정들. 실제 서비스를 할 때 주의해서 적용해야 함.
# 서비스 하기 전, 보안 등의 사항을 위반하지 않는지 체크해야 하는 목록 링크.
# https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# 50 글자로 구성된 임의의 문자열. 비밀번호 암호화 등의 기능에서 사용됨.
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0n%pva5*cd3bmje2wn=##ytczk71_(5qbqeh#luq(i30%sm@hf'

# 디버그 모드 설정 여부. 이 옵션의 값이 True면 디버그 모드로 설정된다.
# 디버그 모드로 설정되면 오류 발생 시 상세 내역을 확인할 수 있다.
# 실제 서비스할 프로젝트에서 디버그 모드를 켜면 안된다.
# 이 옵션의 값이 False면 하단의 ALLOWED_HOSTS를 반드시 설정해야 한다.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 이 프로젝트를 실제로 서비스할 때 배포할 도메인들.
ALLOWED_HOSTS = []


##################################################


# 앱 정의.
# 이 프로젝트에서 사용할 앱을 기록하거나 템플릿 설정, 서버 애플리케이션 설정 등을 한다.

# 이 프로젝트에서 사용할 앱의 목록.
# 앱 설정 클래스(AppConfig)를 등록한다.
# 앱을 생성한 후 이 목록에 등록해야 프로젝트에서 해당 앱을 인식할 수 있다.
INSTALLED_APPS = [
    'summary.apps.SummaryConfig',
    'board.apps.BoardConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 요청-응답 사이에 각종 다양한 처리를 담당하는 앱의 목록.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 최상위 URL 구성 파일이 어디에 있는지 나타내는 옵션.
ROOT_URLCONF = 'practice0928.urls'

# 템플릿 관련 옵션.
# 템플릿 언어 설정, 템플릿 경로 등을 설정한다.
# 여러 개의 템플릿 언어를 설정할 수도 있음.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 템플릿 언어 종류.
        'DIRS': [],  # 템플릿 파일(=.html)을 저장할 경로.
        'APP_DIRS': True,  # 템플릿 파일을 앱 하위 디렉토리에서 찾을지 여부.
        'OPTIONS': {  # 템플릿에서 사용할 앱 설정.
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI 애플리케이션 설정 클래스의 경로.
# 장고에서 지원하는 서버 가동 방식은 ASGI, WSGI가 있는데,
# 기본적으로 WSGI 방식을 사용함.
WSGI_APPLICATION = 'practice0928.wsgi.application'


##################################################


# 데이터베이스 관련 설정.
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# 장고 프로젝트에서 사용할 데이터베이스 목록.
# 하나의 프로젝트에 여러 개의 데이터베이스를 설정할 수도 있음.
# 일반적으로 USER, PASSWORD, HOST, PORT 등을 같이 설정함
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 사용할 데이터베이스의 종류.
        'NAME': BASE_DIR / 'db.sqlite3',  # 데이터베이스 이름.
    },
}


##################################################


# 비밀번호 검증.
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

# 관리자 계정, 사용자 계정 등에서 비밀번호를 설정할 때 검사할 검증기 클래스들의 목록.
# 비밀번호의 유사성 검증, 길이 검증 등을 수행함.
# 필요하다면 직접 임의의 검증기 클래스를 작성해서 추가하여 비밀번호 패턴을 검사할 수도 있음.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


##################################################


# 국제화 및 현지화 설정.
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# 언어 코드. 관리자 페이지 등에서 해당 언어를 적용함.
# 이 옵션이 적용되려면 하단의 USE_I18N 옵션이 True여야함.
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

# 이 프로젝트를 서비스하는 서버 컴퓨터의 시간대.
# 이 옵션이 적용되려면 하단의 USE_TZ 옵션이 True여야함.
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

# 자동 번역 등 국제화 설정 적용 여부.
USE_I18N = True

# 시간대 옵션 적용 여부.
USE_TZ = True


##################################################


# 정적 파일 설정 (CSS, 자바스크립트, 이미지 등)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# 정적 파일을 불러올 때 사용할 URL.
STATIC_URL = 'static/'


##################################################


# PK 필드의 기본 자료형.
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

# 데이터베이스 관련 설정을 할 때, PK 필드를 따로 설정하지 않았다면
# 자동으로 적용시킬 자료형.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
