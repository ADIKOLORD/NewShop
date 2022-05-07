from django.core.validators import MinValueValidator
from django.db import models

'''
Product 
Category
Status
'''


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Product/%Y/%m/%d', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    old_price = models.IntegerField(validators=[MinValueValidator(0)], blank=True)
    pub_date = models.DateField(auto_now=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    watch = models.IntegerField(default=0)

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
