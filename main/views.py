from django.shortcuts import render

from blog.models import Blog
from main.models import Banner, News, Team
from product.models import Product, Category
from product.views import shopfind


def main_page(request):
    if request.method == 'POST':
        return shopfind(request, request.POST['mainsearch'])
    context = {
        'title': 'Home',
        'index': 'active',
        'products': Product.objects.all()[:4],
        'banners': Banner.objects.all(),
        "news": News.objects.all(),
        'categories': Category.objects.all()[:6],
        'categories_show': Category.objects.all(),
        'blogs': Blog.objects.all().filter(is_published=True)[:3]
    }

    return render(request, 'index.html', context)


def about(request):
    if request.method == 'POST':
        return shopfind(request, request.POST['mainsearch'])
    context = {
        'teams': Team.objects.all(),
        'about': 'active',
        'title': 'About',
        'categories_show': Category.objects.all(),

    }

    return render(request, 'about.html', context)
