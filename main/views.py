from django.shortcuts import render

from main.models import Banner, News
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


# def news_header(request):
#     context = {
#         "news": News.objects.all()
#     }
#     return render(request, 'news.html', context)
