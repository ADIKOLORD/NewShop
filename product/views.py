from django.shortcuts import render

# Product App
from product.models import Product


def shop(request, pk):
    if int(pk) == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.all().filter(category_id=pk)
    context = {
        'title': 'Shop',
        'products': products,
    }
    return render(request, 'shop.html', context)
