from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home-главная',
        'content': 'магазин',
    }
    return render(request, 'main/index.html', context)
def about(request):
    context = {
        'title': 'Home-обо мне',
        'content': 'о нас',
        'text_on_page': 'lorem'
    }
    return render(request, 'main/index.html', context)