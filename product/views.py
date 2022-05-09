from django.shortcuts import render, redirect

# Product App
from main.models import News
from product.models import Product, Category


def shopfind(request, word):
    context = {
        'title': 'Shop',
        'shop': 'active',
        'products': Product.objects.all().filter(title__icontains=word),
        'news': News.objects.all(),
        'categories_show': Category.objects.all(),
    }
    return render(request, 'shop.html', context)


def shop(request, pk):
    if request.method == 'POST':
        return shopfind(request, request.POST['word'])

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
        'id': pk

    }
    return render(request, 'shop.html', context)


def shopdetail(request, pk):
    context = {
        'title': 'Detail',
        'categories_show': Category.objects.all(),
        'product': Product.objects.get(pk=pk),
        'products': Product.objects.all()[:7]
    }
    return render(request, 'shop-detail.html', context)
