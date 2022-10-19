from django.shortcuts import render

from .models import Board, Reply


def home(request):
    return render(request, "home.html")


def board_list(request):
    context = {
        # 'board_list': Board.objects.all().reverse(),
        'board_list': Board.objects.all().order_by('-date'),
    }
    return render(request, "board/list.html", context)


def board_detail(request, num):
    context = {
        'board': Board.objects.get(num=num),
        'reply_list': Board.objects.get(num=num).reply_set.all(),
        # 'reply_list': Reply.objects.filter(board_id=num),
    }
    return render(request, "board/detail.html", context)


def board_summary(request):
    return render(request, "board/summary.html")
