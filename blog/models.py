from django.db import models

from product.models import Product

'''
Blog
Comment

'''


class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Blog/%m/%d', blank=True)
    is_published = models.BooleanField(default=False)
    watch = models.IntegerField(default=0)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
