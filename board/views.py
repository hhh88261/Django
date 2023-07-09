from django.shortcuts import render

# Create your views here.

def board_list(request):
    return render(request, 'board.html')

def gallery(request):
    return render(request, 'gallery.html')
