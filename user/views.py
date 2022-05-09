from django.shortcuts import render

from product.models import Product, Category

# User App
p = Product.objects.all()[:5]


def cart(request):
    sum_product = 0
    for i in p:
        sum_product += i.price
    context = {
        'title': 'Cart',
        'products': p,
        'sum_pro': sum_product - 52,
        'categories_show': Category.objects.all(),
    }

    return render(request, 'cart.html', context)


def dele(request, id):
    global p
    n = []
    for i in p:
        if i.id != id:
            n.append(i)
    p = n
    sum_product = 0
    for i in p:
        sum_product += i.price
    context = {
        'title': 'Cart',
        'products': p,
        'sum_pro': sum_product - 52,
        'categories_show': Category.objects.all(),

    }

    return render(request, 'cart.html', context)


def checkout(request):
    context = {
        'title': 'Checkout',
        'categories_show': Category.objects.all(),

    }
    return render(request, 'checkout.html', context)