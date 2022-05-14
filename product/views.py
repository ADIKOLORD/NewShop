from django.shortcuts import render

# Product App

from main.models import News
from product.models import Product, Category
from user.models import MyUser


def shopfind(request, word):
    context = {
        'title': 'Shop',
        'shop': 'active',
        'products': Product.objects.all().filter(title__icontains=word),
        'news': News.objects.all(),
        'categories_show': Category.objects.all(),
    }
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),
        })
    return render(request, 'shop.html', context)


def shop(request, pk=0):
    for cat in Category.objects.all():
        cat.count = Product.objects.all().filter(category_id=cat.id).count()
        cat.save()

    if request.method == 'POST':
        try:
            return shopfind(request, request.POST['word'])
        except:
            return shopfind(request, request.POST['mainsearch'])

    if int(pk) == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.all().filter(category_id=pk)

    context = {
        'title': 'Shop',
        'shop': 'active',
        'products': products,
        'news': News.objects.all(),
        'categories_show': Category.objects.all(),
        'id': pk,
        'par1': sum([i.count for i in Category.objects.all().filter(parent=1)]),
        'par2': sum([i.count for i in Category.objects.all().filter(parent=2)]),
        'par3': sum([i.count for i in Category.objects.all().filter(parent=3)]),
        'par4': sum([i.count for i in Category.objects.all().filter(parent=4)]),

    }
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),
        })

    return render(request, 'shop.html', context)


def shopdetail(request, pk):
    context = {
        'title': 'Detail',
        'categories_show': Category.objects.all(),
        'product': Product.objects.get(pk=pk),
        'products': Product.objects.all()[:7],
        "news": News.objects.all(),

    }
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),
        })
    return render(request, 'shop-detail.html', context)
