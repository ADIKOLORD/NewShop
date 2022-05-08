from django.shortcuts import render

from main.models import Banner, News, Team
from product.models import Product, Category


def main_page(request):
    context = {
        'title': 'Home',
        'products': Product.objects.all()[:4],
        'banners': Banner.objects.all(),
        "news": News.objects.all(),
        'categories': Category.objects.all()[:6],
    }
    return render(request, 'index.html', context)


def header(request):
    context = {
        "news": News.objects.all()
    }
    return render(request, 'header.html', context)



def about(request):
    context = {
        'teams': Team.objects.all(),
        'about': 'active',
        'title': 'About',
    }

    return render(request, 'about.html', context)


def cate_product(request):
    context = {
        'parent_categories': Category.objects.all()
    }
    return render(request, 'cate_product.html', context)