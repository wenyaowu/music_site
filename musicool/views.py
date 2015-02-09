from django.shortcuts import render


def index(request):
    context_dict = {}
    return render(request, 'musicool/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'musicool/about.html', context_dict)