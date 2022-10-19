from django.shortcuts import render


# Create your views here.
def home(request):
    """홈 화면으로 이동하는 뷰 함수."""
    return render(request, "summary/home.html")


def setting(request):
    """데이터베이스 연동 설정 화면으로 이동하는 뷰 함수."""
    return render(request, "summary/setting.html")


def model(request):
    """모델 페이지로 이동하는 뷰 함수."""
    return render(request, "summary/model.html")

def migration(request):
    """마이그레이션 페이지로 이동하는 뷰 함수."""
    return render(request, "summary/migration.html")

def manipulation(request):
    """데이터베이스 조작 페이지로 이동하는 뷰 함수."""
    return render(request, "summary/manipulation.html")