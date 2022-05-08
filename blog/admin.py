from django.contrib import admin
from django.db.models import QuerySet

from blog.models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # exclude -> Кайсы полялар добавить эткенде корунбосун
    exclude = ['watch', 'pub_date', 'like']

    # readonly_fields -> Кайсыларды изменить этсе болбойт!
    readonly_fields = []  # watch

    # list_display -> Отображение на панеле
    list_display = ('author', 'is_published', 'watch', 'like')

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['author']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('author', 'text', 'title')

    # list_editable -> Панелде сразу редактирование кылса болот
    # list_editable = ('price',)

    # list_filter -> Фильтр для отображения
    list_filter = ('is_published',)

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


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # exclude -> Кайсы полялар добавить эткенде корунбосун
    exclude = ['pub_date']

    # readonly_fields -> Кайсыларды изменить этсе болбойт!
    readonly_fields = []  # watch

    # list_display -> Отображение на панеле
    list_display = ('name', 'product', )

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ('name', 'product', )

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('name', 'comment', 'product', )

    # list_editable -> Панелде сразу редактирование кылса болот
    # list_editable = ('price',)

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


admin.site.register(Comment, CommentAdmin)
