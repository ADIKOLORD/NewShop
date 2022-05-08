from django.shortcuts import render

from blog.models import Blog
from main.models import Banner, News, Team
from product.models import Product, Category


def main_page(request):
    context = {
        'title': 'Home',
        'products': Product.objects.all()[:4],
        'banners': Banner.objects.all(),
        "news": News.objects.all(),
        'categories': Category.objects.all()[:6],
        'blogs': Blog.objects.all().filter(is_published=True)[:3]
    }

    return render(request, 'index.html', context)


def header(request):
    context = {
        "news": News.objects.all(),
    }
    return render(request, 'header.html', context)


def about(request):
    context = {
        'teams': Team.objects.all(),
        'about': 'active',
        'title': 'About',
    }

    return render(request, 'about.html', context)


def cate(request):
    context = {
        "one": [1, 3, 4, 5, 6, ],
        'two': Category.objects.all(),
        'three': Category.objects.all().filter(parent=3),
        'four': Category.objects.all().filter(parent=4),
    }

    return render(request, 'cate_product.html', context)
