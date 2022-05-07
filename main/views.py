from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'index.html', context)
