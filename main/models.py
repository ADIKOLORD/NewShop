from django.db import models

from product.models import Product, Category

'''
Discount
Banner
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
        return self.title.id

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннер'
