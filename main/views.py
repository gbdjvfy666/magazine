from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):

    categories = Categories.objects.all

    context = {
        'title': 'Home-главная',
        'content': 'магазин',
        'categories': categories
    }
    return render(request, 'main/index.html', context)
def about(request):
    context = {
        'title': 'Home-обо мне',
        'content': 'о нас',
        'text_on_page': 'lorem'
    }
    return render(request, 'main/index.html', context)