from django.shortcuts import render

from django.http import HttpResponse


# def index(request):
#     return HttpResponse('Игорь')


def index(request):
    tags = 'hexslet_django_blog'
    return render(
        request,
        'articles/base.html',
        context={'tags': tags},
    )
