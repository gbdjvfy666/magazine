from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'главная страница'
    }
    return render(request, 'main/index.html', context)
def about(request):
    return HttpResponse('ABOBA')