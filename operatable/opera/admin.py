from django.contrib import admin


from .models import Tables, Scene, Table


class TablesInline(admin.TabularInline):
    model = Tables


class SceneInline(admin.TabularInline):
    model = Scene


class TableAdmin(admin.ModelAdmin):
    inlines = [
        TablesInline,
        SceneInline
    ]

admin.site.register(Table, TableAdmin)
# admin.site.register(Tables)
# admin.site.register(Scene)

# class OperaInline(admin.TabularInline):
#     model = Opera
#
#
# class BaletInline(admin.TabularInline):
#     model = Bal
#
# class SceneInline(admin.TabularInline):
#     model = Scene
#
#
#
# class TableAdmin(admin.ModelAdmin):
#     inlines = [
#         OperaInline,
#         BaletInline,
#         SceneInline,
#     ]
#
#
# admin.site.register(Table, TableAdmin)
# admin.site.register(Scene)
# admin.site.register(Opera)
# admin.site.register(Bal)

admin.site.site_header = "Театр Оперы и Балета"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать в админку"
