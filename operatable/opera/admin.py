from django.contrib import admin
from django import forms

from .models import Tables, Table


class TablesInline(admin.TabularInline):
    model = Tables


class TableAdmin(admin.ModelAdmin):
    inlines = [
        TablesInline,
        # SceneInline
    ]
    list_display = ('date', 'day',)


admin.site.register(Table, TableAdmin)

admin.site.site_header = "Театр Оперы и Балета"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать в админку"
