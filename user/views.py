from django.shortcuts import render

from product.models import Product, Category

# User App
p = []  # Products in Cart
wishlist_product = []


def wishlist_add(request, pk):
    global wishlist_product
    for wp in Product.objects.all():
        if wp.id == pk and wp not in wishlist_product:
            wishlist_product.append(wp)

    context = {
        'title': 'Wishlist',
        'wp': wishlist_product,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }

    return render(request, 'wishlist.html', context)


def wishlist_del(request, pk):
    global wishlist_product
    vrem = []
    for wp in wishlist_product:
        if wp.id != pk:
            vrem.append(wp)
    wishlist_product = vrem

    context = {
        'title': 'Wishlist',
        'wp': wishlist_product,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }

    return render(request, 'wishlist.html', context)


def cart(request):
    sum_product = sum([i.price for i in p])  # sum all products in Cart

    context = {
        'title': 'Cart',
        'products': p,
        'sum_pro': sum_product - 52,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }

    return render(request, 'cart.html', context)


def cart_add(request, id):
    global p

    wishlist_del(request, id)
    for pr in Product.objects.all():
        if pr.id == id and pr not in p:
            p.append(pr)
    sum_product = sum([i.price for i in p])  # sum all products in Cart
    context = {
        'title': 'Cart',
        'products': p,
        'sum_pro': sum_product - 52,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),

    }

    return render(request, 'cart.html', context)


def cart_dele(request, id):
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
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),

    }

    return render(request, 'cart.html', context)


def checkout(request):
    sum_product = sum([i.price for i in p])  # sum all products in Cart
    context = {
        'title': 'Checkout',
        'categories_show': Category.objects.all(),
        'buy_products': p,
        'sum_pro': sum_product - 52,
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),


    }
    return render(request, 'checkout.html', context)
