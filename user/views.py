from django.shortcuts import render

from product.models import Product


# User App

def cart(request):
    p = Product.objects.all()[:5]
    sum_product = 0
    for i in p:
        sum_product += i.price
    context = {
        'title': 'Cart',
        'products': Product.objects.all()[:5],
        'sum_pro': sum_product,
        'sum_last': sum_product - 52,
    }

    return render(request, 'cart.html', context)

