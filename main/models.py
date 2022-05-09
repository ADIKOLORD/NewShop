from django.db import models

from product.models import Product, Category

'''
Discount
Banner
Team
'''


class News(models.Model):
    news = models.CharField(max_length=250, verbose_name='Что нового')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.news

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='Banner/%m/%d', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннер'


class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='OURTEAM/%m/%d')
    description = models.TextField()
    site = models.URLField(max_length=200)
    POSITION = (
        ('DIRECTOR', 'DIRECTOR'),
        ('DIRECTOR', 'MENEDJER'),
        ('WEB DEVELOPER', 'WEB DEVELOPER'),
        ('DESING', 'DESING'),
        ('BACK END DEVELOPER', 'BACK END DEVELOPER'),
    )
    position = models.CharField(max_length=50, choices=POSITION, default='WEB DEVELOPER')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Команда'