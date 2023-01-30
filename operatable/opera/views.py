from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
import re
import datetime


# Create your views here.
def index(request):
    weekday_dict = {0: "Пн", 1: "Вт", 2: "Ср", 3: "Чт", 4: "Пт", 5: "Сб", 6: "Вс"}
    yesterday = datetime.datetime.now() - datetime.timedelta(1)
    new_date = datetime.datetime.now() + datetime.timedelta(6)
    weekday = weekday_dict[new_date.weekday()]
    if Table.objects.filter(date=yesterday).count():
        Table.objects.filter(date=yesterday).delete()
        Table.objects.create(date=new_date, day=weekday)
    if Scene.objects.filter(data_nascimento=yesterday).count():
        Scene.objects.filter(data_nascimento=yesterday).delete()

    posts = Table.objects.all()
    opera = Tables.objects.all()
    scene = Scene.objects.all()
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
    friday_text_b = ""
    saturday_text_b = ""
    sunday_text_b = ""
    monday_id = ""
    tuesday_id = ""
    wednesday_id = ""
    thursday_id = ""
    friday_id = ""
    saturday_id = ""
    sunday_id = ""
    hhh = ""
    for h in Scene.objects.filter().values('data_nascimento'):
        hhh = (f"{h['data_nascimento']}")
    for test in Table.objects.filter(day="Пн").values("id"):
        monday_id = (f"{test['id']}")
    for test in Table.objects.filter(day="Вт").values("id"):
        tuesday_id = (f"{test['id']}")
    for test in Table.objects.filter(day="Ср").values("id"):
        wednesday_id = (f"{test['id']}")
    for test in Table.objects.filter(day="Чт").values("id"):
        thursday_id = (f"{test['id']}")
    for test in Table.objects.filter(day="Пт").values("id"):
        friday_id  = (f"{test['id']}")
    for test in Table.objects.filter(day="Сб").values("id"):
        saturday_id  = (f"{test['id']}")
    for test in Table.objects.filter(day="Вс").values("id"):
        sunday_id  = (f"{test['id']}")

    for a in Tables.objects.filter(table_id=monday_id):
        monday_text = monday_text + (f"{a.opera}") + "\n"
    for b in Tables.objects.filter(table_id=tuesday_id):
        tuesday_text = tuesday_text + (f"{b.opera}") + "\n"
    for c in Tables.objects.filter(table_id=wednesday_id):
        wednesday_text = wednesday_text + (f"{c.opera}") + "\n"
    for d in Tables.objects.filter(table_id=thursday_id):
        thursday_text = thursday_text + (f"{d.opera}") + "\n"
    for e in Tables.objects.filter(table_id=friday_id):
        friday_text = friday_text + (f"{e.opera}") + "\n"
    for f in Tables.objects.filter(table_id=saturday_id):
        saturday_text = saturday_text + (f"{f.opera}") + "\n"
    for g in Tables.objects.filter(table_id= sunday_id):
        sunday_text = sunday_text + (f"{g.opera}") + "\n"

    for a in Tables.objects.filter(table_id=monday_id):
        monday_text_b = monday_text_b + (f"{a.balet}") + "\n"
    for b in Tables.objects.filter(table_id=tuesday_id):
        tuesday_text_b = tuesday_text_b + (f"{b.balet}") + "\n"
    for c in Tables.objects.filter(table_id=wednesday_id):
        wednesday_text_b = wednesday_text_b + (f"{c.balet}") + "\n"
    for d in Tables.objects.filter(table_id=thursday_id):
        thursday_text_b = thursday_text_b + (f"{d.balet}") + "\n"
    for e in Tables.objects.filter(table_id=friday_id):
        friday_text_b = friday_text_b + (f"{e.balet}") + "\n"
    for f in Tables.objects.filter(table_id=saturday_id):
        saturday_text_b = saturday_text_b + (f"{f.balet}") + "\n"
    for g in Tables.objects.filter(table_id=sunday_id):
        sunday_text_b = sunday_text_b + (f"{g.balet}") + "\n"

    return render(request, 'opera/index.html',
                  {'posts': posts, 'opera': opera, 'scene': scene, 'monday_text': monday_text,
                   'tuesday_text': tuesday_text, 'monday_id': int(monday_id),
                   'tuesday_id': int(tuesday_id), 'wednesday_id': int(wednesday_id), 'wednesday_text': wednesday_text,
                   'monday_text_b': monday_text_b, 'tuesday_text_b': tuesday_text_b,
                   'wednesday_text_b': wednesday_text_b,
                   'thursday_id': int(thursday_id), 'thursday_text': thursday_text, 'friday_id': int(friday_id),
                   'friday_text': friday_text,'thursday_text_b':thursday_text_b, 'friday_text_b': friday_text_b,
                   'saturday_text_b':saturday_text_b,'sunday_text_b':sunday_text_b,'saturday_text':saturday_text,
                   'sunday_text':sunday_text,'saturday_id':int(saturday_id),'sunday_id':int(sunday_id),'hhh':hhh})


"Для 404 ошибки"


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
