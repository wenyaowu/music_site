from django.shortcuts import render
from models import *


def index(request):

    hot_albums = Album.objects.order_by('-likes')[:4]

    context_dict = {'hot_albums': hot_albums}
    return render(request, 'musicool/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'musicool/about.html', context_dict)



