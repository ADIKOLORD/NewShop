from django.db import models


# User model
from product.models import Product


class MyUser(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    cart = models.ManyToManyField(Product, related_name='carts', blank=True)
    wishlist = models.ManyToManyField(Product, related_name='wishlists', blank=True)

    def __str__(self):
        return self.name

