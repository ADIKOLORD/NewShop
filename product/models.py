from django.core.validators import MinValueValidator
from django.db import models

'''
Product 
Category
Status
'''


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField()
    image = models.ImageField(upload_to='Product/%Y/%m/%d', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Цена')
    old_price = models.IntegerField(blank=True, default=0)
    pub_date = models.DateField(auto_now=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    watch = models.IntegerField(default=0, verbose_name='Просмотры')

    # wishlist = models.ManyToManyField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    BIGCATEGORIES = (
        ('1', 'TOP'),
        ('2', 'BOTTOM'),
        ('3', 'CLOTHING'),
        ('4', 'ACCESSORIES'),
    )
    parent = models.CharField(max_length=1,
                              choices=BIGCATEGORIES,
                              default=3,
                              verbose_name='Группа', )
    image = models.ImageField(upload_to='Product/Category/%m/%d', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Status(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
