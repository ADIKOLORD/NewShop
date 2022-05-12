from django.shortcuts import render, redirect

# Product App
from django.views.generic import DetailView

from main.models import News
from product.models import Product, Category
from user.views import p

for i in Category.objects.all():
    a = Category.objects.get(pk=i.id)
    a.count = Product.objects.all().filter(category_id=i.id).count()
    a.save()


def shopfind(request, word):
    context = {
        'title': 'Shop',
        'shop': 'active',
        'products': Product.objects.all().filter(title__icontains=word),
        'news': News.objects.all(),
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }
    return render(request, 'shop.html', context)


def shop(request, pk=0):
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
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),

    }

    return render(request, 'shop.html', context)


def shopdetail(request, pk):
    context = {
        'title': 'Detail',
        'categories_show': Category.objects.all(),
        'product': Product.objects.get(pk=pk),
        'products': Product.objects.all()[:7],
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }
    return render(request, 'shop-detail.html', context)
