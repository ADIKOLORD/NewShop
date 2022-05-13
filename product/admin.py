from django.contrib import admin
from django.db.models import QuerySet

from product.models import *

# class ModelAdmin(admin.ModelAdmin):
'''
class ModelAdmin(admin.ModelAdmin):
    fields -> Кайсы поляларды толтурганга болот. Же добавить эткенде кайсылар корунсун

    exclude -> Кайсы полялар добавить эткенде корунбосун

    readonly_fields -> Кайсыларды изменить этсе болбойт! 

    list_display -> Отображение на панеле

    list_display_links -> Переобразовать в ссылку

    search_fields -> Поиск болгондо кайсылардан издеш керек!

    list_editable -> Панелде сразу редактирование кылса болот

    list_filter -> Фильтр для отображения

    list_per_page -> Бир страницада канча запись болуш керек

    prepopulated_fields -> Ключ болуп турган поляга, значениеде турган полянын ичиндеги жазылат!

    actions -> Кайсы дествиялар болуш керек

    # Добавление дествии
    @admin.action(description='Отображение на панеле действии')
    def имя_что_делает(self, request, qs: QuerySet):
        pass

'''


class ProductAdmin(admin.ModelAdmin):
    '''
    Для настройки админской панели!
    '''

    # exclude -> Кайсы полялар добавить эткенде корунбосун
    exclude = ['watch', 'pub_date']

    # readonly_fields -> Кайсыларды изменить этсе болбойт!
    readonly_fields = []  # watch

    # list_display -> Отображение на панеле
    list_display = ('title', 'price', 'old_price', 'category', 'watch')

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['title', 'category']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('title', 'description',)

    # list_editable -> Панелде сразу редактирование кылса болот
    list_editable = ('price', 'old_price',)

    # list_filter -> Фильтр для отображения
    list_filter = ('status', 'category',)

    # list_per_page -> Бир страницада канча запись болуш керек
    list_per_page = 15

    # actions -> Кайсы дествиялар болуш керек
    actions = [
        'set_clone_model',
    ]

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()

    """
    actions = ['set_category_man',
               'set_category_woman',
               'set_category_sport',
               'set_category_electric',
               'set_clone_model',
               ]

    # Добавление дествии
    @admin.action(description='Установить категорию Sport')
    def set_category_sport(self, request, qs: QuerySet):
        count_updates = qs.update(category=3)
        # self.message_user -> Функция болгондо кандай сообщение чыгарына жооп берет.
        self.message_user(request,
                          f'Было обновлено {count_updates} записей', )

    @admin.action(description='Установить категорию Man')
    def set_category_man(self, request, qs: QuerySet):
        qs.update(category=1)

    @admin.action(description='Установить категорию Woman')
    def set_category_woman(self, request, qs: QuerySet):
        qs.update(category=2)

    @admin.action(description='Установить категорию Electric')
    def set_category_electric(self, request, qs: QuerySet):
        qs.update(category=4)

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()
    """


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    # list_display -> Отображение на панеле
    list_display = ['title', 'parent', 'count']
    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ['title']
    # list_filter -> Фильтр для отображения
    list_filter = ['parent']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Status)
