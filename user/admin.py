from django.contrib import admin

from user.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

    list_display_links = ['name', 'email']

    filter_horizontal = ['cart', 'wishlist']

    search_fields = ('name', 'email')

    list_per_page = 10


admin.site.register(MyUser, MyUserAdmin)
