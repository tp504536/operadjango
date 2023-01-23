from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


# Create your views here.
def index(request):
    posts = Table.objects.all()
    #opera = Opera.objects.all()
    scene = Scene.objects.all()


    return render(request, 'opera/index.html', {'posts': posts, 'scene': scene})


"Для 404 ошибки"


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
