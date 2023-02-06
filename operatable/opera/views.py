from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
import re
import datetime


def get_weekday(date):
    weekday_dict = {0: "Пн", 1: "Вт", 2: "Ср", 3: "Чт", 4: "Пт", 5: "Сб", 6: "Вс"}
    return weekday_dict[date]


def get_dayofweek_id(day):
    for test in Table.objects.filter(day=day).values("id"):
        dayofweek_id = (f"{test['id']}")
    return dayofweek_id


# Create your views here.
def index(request):
    stack = []
    yesterday = datetime.datetime.now() - datetime.timedelta(1)
    while Table.objects.filter(date=yesterday).count():
        stack.append(yesterday + datetime.timedelta(7))
        Table.objects.filter(date=yesterday).delete()
        yesterday = yesterday - datetime.timedelta(1)
    while stack:
        date = stack.pop()
        Table.objects.create(date=date, day=get_weekday(date.weekday()))
    posts = Table.objects.all()
    opera = Tables.objects.all()
    monday_text = tuesday_text = wednesday_text = thursday_text = friday_text = saturday_text = sunday_text = \
        monday_text_b = tuesday_text_b = wednesday_text_b = thursday_text_b = friday_text_b = saturday_text_b = \
        sunday_text_b = monday_text_s = tuesday_text_s = wednesday_text_s = thursday_text_s = friday_text_s = \
        saturday_text_s = sunday_text_s = ""
    monday_id = get_dayofweek_id("Пн")
    tuesday_id = get_dayofweek_id("Вт")
    wednesday_id = get_dayofweek_id("Ср")
    thursday_id = get_dayofweek_id("Чт")
    friday_id = get_dayofweek_id("Пт")
    saturday_id = get_dayofweek_id("Сб")
    sunday_id = get_dayofweek_id("Вс")
    monday_text1 = []
    tuesday_text1 = []
    wednesday_text1 = []

    for a in Tables.objects.filter(table_id=monday_id):
        monday_text_s = monday_text_s + (f"{a.scena}") + "\n"
        monday_text1.append((f"{a.opera}"))
        monday_text_b = monday_text_b + (f"{a.balet}") + "\n"
    for b in Tables.objects.filter(table_id=tuesday_id):
        tuesday_text_s = tuesday_text_s + (f"{b.scena}") + "\n"
        tuesday_text1.append((f"{b.opera}"))
        tuesday_text_b = tuesday_text_b + (f"{b.balet}") + "\n"
    for c in Tables.objects.filter(table_id=wednesday_id):
        wednesday_text_s = wednesday_text_s + (f"{c.scena}") + "\n"
        wednesday_text1.append((f"{c.opera}"))
        wednesday_text_b = wednesday_text_b + (f"{c.balet}") + "\n"
    for d in Tables.objects.filter(table_id=thursday_id):
        thursday_text_s = thursday_text_s + (f"{d.scena}") + "\n"
        thursday_text = thursday_text + (f"{d.opera}") + "\n"
        thursday_text_b = thursday_text_b + (f"{d.balet}") + "\n"
    for e in Tables.objects.filter(table_id=friday_id):
        friday_text_s = friday_text_s + (f"{e.scena}") + "\n"
        friday_text = friday_text + (f"{e.opera}") + "\n"
        friday_text_b = friday_text_b + (f"{e.balet}") + "\n"
    for f in Tables.objects.filter(table_id=saturday_id):
        saturday_text_s = saturday_text_s + (f"{f.scena}") + "\n"
        saturday_text = saturday_text + (f"{f.opera}") + "\n"
        saturday_text_b = saturday_text_b + (f"{f.balet}") + "\n"
    for g in Tables.objects.filter(table_id=sunday_id):
        sunday_text_s = sunday_text_s + (f"{g.scena}") + "\n"
        sunday_text = sunday_text + (f"{g.opera}") + "\n"
        sunday_text_b = sunday_text_b + (f"{g.balet}") + "\n"

    return render(request, 'opera/index.html',
                  {'posts': posts, 'opera': opera, 'monday_text': monday_text,
                   'tuesday_text': tuesday_text, 'monday_id': int(monday_id),
                   'tuesday_id': int(tuesday_id), 'wednesday_id': int(wednesday_id), 'wednesday_text': wednesday_text,
                   'monday_text_b': monday_text_b, 'tuesday_text_b': tuesday_text_b,
                   'wednesday_text_b': wednesday_text_b,
                   'thursday_id': int(thursday_id), 'thursday_text': thursday_text, 'friday_id': int(friday_id),
                   'friday_text': friday_text, 'thursday_text_b': thursday_text_b, 'friday_text_b': friday_text_b,
                   'saturday_text_b': saturday_text_b, 'sunday_text_b': sunday_text_b, 'saturday_text': saturday_text,
                   'sunday_text': sunday_text, 'saturday_id': int(saturday_id), 'sunday_id': int(sunday_id),
                   'sunday_text_s': sunday_text_s, 'monday_text_s': monday_text_s, 'tuesday_text_s': tuesday_text_s,
                   'wednesday_text_s': wednesday_text_s, 'thursday_text_s': thursday_text_s,
                   'friday_text_s': friday_text_s, 'saturday_text_s': saturday_text_s, 'monday_text1': monday_text1,
                   'tuesday_text1': tuesday_text1,'wednesday_text1':wednesday_text1})


"Для 404 ошибки"


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
