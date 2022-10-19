from django.shortcuts import render

# Create your views here.
def background_knowledge(request):
    """배경 지식 페이지로 이동하는 뷰 함수."""
    return render(request, "background/knowledge.html")
