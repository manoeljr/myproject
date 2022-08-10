from django.shortcuts import render

from .models import Board


def index(request):
    boards = Board.objects.all()
    return render(request, 'boards/index.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/topics.html', {'board': board})



