from django.shortcuts import render
from product.models import Product

def main_page(request):
    context = {
        'title': 'Home',
        'products': Product.objects.all()[:4]
    }
    return render(request, 'index.html', context)
