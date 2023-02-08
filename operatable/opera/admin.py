from django.contrib import admin
from django import forms

from .models import Tables, Table, Opera, Operatable,Rep



class RepInline(admin.TabularInline):
    model = Rep
class TablesInline(admin.TabularInline):
    model = Tables


class OperaInline(admin.TabularInline):
    model = Opera

class RepAdmin(admin.ModelAdmin):
    inlines = [
        RepInline,
    ]
class OperaAdmin(admin.ModelAdmin):
    inlines = [
        OperaInline,
    ]


class TableAdmin(admin.ModelAdmin):
    inlines = [
        TablesInline,
    ]
    list_display = ('date', 'day',)


admin.site.register(Table, TableAdmin)
admin.site.register(Operatable, OperaAdmin)
admin.site.register(Rep, RepAdmin)

admin.site.site_header = "Театр Оперы и Балета"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать в админку"
