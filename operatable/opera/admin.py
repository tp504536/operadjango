from django.contrib import admin
from django import forms
from django.forms import TextInput, Textarea
from django.db import models
from .models import Tables, Table,OperaLesson,TableLesson,TimeLesson




class TablesInline(admin.TabularInline):
    model = Tables
class OperaLessonInline(admin.TabularInline):
    model = OperaLesson
    extra = 45
class TableLessonInline(admin.TabularInline):
    model = TableLesson
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '10'})},

    }



class TableLessAdmin(admin.ModelAdmin):
    inlines = [
        TableLessonInline,
        OperaLessonInline,
    ]

class TableAdmin(admin.ModelAdmin):
    inlines = [
        TablesInline,
    ]
    list_display = ('date', 'day',)





admin.site.register(Table, TableAdmin)
admin.site.register(TimeLesson, TableLessAdmin)



admin.site.site_header = "Театр Оперы и Балета"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать в админку"
