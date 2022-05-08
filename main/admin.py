from django.contrib import admin
from django.db.models import QuerySet

from main.models import News, Banner, Team


class NewsAdmin(admin.ModelAdmin):
    # list_display -> Отображение на панеле
    list_display = ['news', 'product', 'category']
    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['news', 'product', 'category']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ['news', 'product', 'category']

    # list_filter -> Фильтр для отображения
    list_filter = ['category']

    # actions -> Кайсы дествиялар болуш керек
    actions = [
        'set_clone_model',
    ]

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()


admin.site.register(News, NewsAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title']
    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ['title', 'text']
    # actions -> Кайсы дествиялар болуш керек
    actions = [
        'set_clone_model',
    ]

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()


admin.site.register(Banner, BannerAdmin)


class TeamAdmin(admin.ModelAdmin):
    # list_display -> Отображение на панеле
    list_display = ['name', 'position']
    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['name', 'position']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ['name', 'description', ]

    # list_filter -> Фильтр для отображения
    list_filter = ['position']

    # actions -> Кайсы дествиялар болуш керек
    actions = [
        'set_clone_model',
    ]

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()


admin.site.register(Team, TeamAdmin)
