from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


# Create your views here.
def index(request):
    posts = Table.objects.all()
    opera = Tables.objects.all()
    scene = Scene.objects.all()
    # monday_text = Tables.objects.filter(table_id='1')
    # tuesday_text = Tables.objects.filter(table_id='2')
    monday_text = ""
    tuesday_text = ""
    wednesday_text = ""
    thursday_text = ""
    friday_text = ""
    saturday_text = ""
    sunday_text = ""
    monday_text_b = ""
    tuesday_text_b = ""
    wednesday_text_b = ""
    thursday_text_b = ""
    friday_text_b= ""
    saturday_text_b = ""
    sunday_text_b= ""
    monday_id = ""
    tuesday_id = ""
    wednesday_id = ""
    for test in Table.objects.filter(day="Понедельник").values("id"):
        monday_id = (f"{test['id']}")
    for test in Table.objects.filter(day="Вторник").values("id"):
        tuesday_id = (f"{test['id']}")
    for test in Table.objects.filter(day="Среда").values("id"):
        wednesday_id = (f"{test['id']}")

    for a in Tables.objects.filter(table_id=monday_id):
        monday_text = monday_text + (f"{a.opera}") + "\n"
    for b in Tables.objects.filter(table_id=tuesday_id):
        tuesday_text = tuesday_text + (f"{b.opera}") + "\n"
    for c in Tables.objects.filter(table_id=wednesday_id):
        wednesday_text = wednesday_text + (f"{c.opera}") + "\n"

    for a in Tables.objects.filter(table_id=monday_id):
        monday_text_b = monday_text_b + (f"{a.balet}") + "\n"
    for b in Tables.objects.filter(table_id=tuesday_id):
        tuesday_text_b = tuesday_text_b + (f"{b.balet}") + "\n"
    for c in Tables.objects.filter(table_id=wednesday_id):
        wednesday_text_b = wednesday_text_b + (f"{c.balet}") + "\n"

    return render(request, 'opera/index.html',
                  {'posts': posts, 'opera': opera, 'scene': scene, 'monday_text': monday_text,
                   'tuesday_text': tuesday_text, 'monday_id': int(monday_id),
                   'tuesday_id': int(tuesday_id), 'wednesday_id': int(wednesday_id), 'wednesday_text': wednesday_text,
                   'monday_text_b': monday_text_b, 'tuesday_text_b': tuesday_text_b, 'wednesday_text_b': wednesday_text_b
                   })


"Для 404 ошибки"


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
