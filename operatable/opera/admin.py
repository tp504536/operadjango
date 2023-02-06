from django.contrib import admin
from django import forms

from .models import Tables,Table


class TablesInline(admin.TabularInline):
    model = Tables


# class BalInline(admin.TabularInline):
#     model = Bal
#
#
# class SceneInline(admin.TabularInline):
#     model = Scene
#

class TableAdmin(admin.ModelAdmin):
    inlines = [
        TablesInline,
        # SceneInline
    ]
    list_display = ('date',)


# class BalAdmin(admin.ModelAdmin):
#     list_display = ('table',)
#
#
# class SceneAdmin(admin.ModelAdmin):
#     list_display = ('data_nascimento',)


admin.site.register(Table, TableAdmin)
# admin.site.register(Bal, BalAdmin)
# admin.site.register(Scene, SceneAdmin)

admin.site.site_header = "Театр Оперы и Балета"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать в админку"
