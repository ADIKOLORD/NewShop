
from django.views.generic import ListView

from blog.models import Blog
from main.models import Banner, News, Team
from product.models import Product, Category
from product.views import shopfind
from user.models import MyUser



# func show main_page
# def main_page(request):
#     if request.method == 'POST':
#         return shopfind(request, request.POST['mainsearch'])
#     context = {
#         'title': 'Home',
#         'index': 'active',
#         'products': Product.objects.all()[:4],
#         'banners': Banner.objects.all(),
#         "news": News.objects.all(),
#         'categories': Category.objects.all()[:6],
#         'categories_show': Category.objects.all(),
#         'blogs': Blog.objects.all().filter(is_published=True)[:3],
#         'count_cart': len(p),
#         'cart_products': p,
#         'sum_cart': sum([i.price for i in p]),
#     }
#
#     return render(request, 'index.html', context)


# class show main_page

class Main(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories_show'
    for i in Category.objects.all():
        a = Category.objects.get(pk=i.id)
        a.count = Product.objects.all().filter(category_id=i.id).count()
        a.save()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update({
            'title': 'Home',
            'index': 'active',
            'products': Product.objects.all()[:4],
            'banners': Banner.objects.all(),
            "news": News.objects.all(),
            'categories': Category.objects.all()[:6],
            'blogs': Blog.objects.all().filter(is_published=True)[:3],
            'categories_show': Category.objects.all(),

        })
        if self.request.user.is_authenticated:
            user = MyUser.objects.get(name=self.request.user.username)
            context.update({
                'count_cart': user.cart.count(),
                'cart_products': user.cart.all(),
                'sum_cart': sum([i.price for i in user.cart.all()]),
            })

        return context

    def post(self, request):
        return shopfind(request, request.POST['mainsearch'])


# func show about
# def about(request):
#     if request.method == 'POST':
#         return shopfind(request, request.POST['mainsearch'])
#     context = {
#         'teams': Team.objects.all(),
#         'about': 'active',
#         'title': 'About',
#         'categories_show': Category.objects.all(),
#         'count_cart': len(p),
#         'cart_products': p,
#         'sum_cart': sum([i.price for i in p]),
#
#     }
#
#     return render(request, 'about.html', context)


# class show about

class About(ListView):
    model = Team
    template_name = 'about.html'
    context_object_name = 'teams'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context.update({
            'about': 'active',
            'title': 'About',
            'categories_show': Category.objects.all(),

        })
        if self.request.user.is_authenticated:
            user = MyUser.objects.get(name=self.request.user.username)
            context.update({
                'count_cart': user.cart.count(),
                'cart_products': user.cart.all(),
                'sum_cart': sum([i.price for i in user.cart.all()]),
            })
        return context

    def post(self, request):
        return shopfind(request, request.POST['mainsearch'])


# func show service
# def service(request):
#     context = {
#         'title': 'Service',
#         'service': 'active',
#         'categories_show': Category.objects.all(),
#         'count_cart': len(p),
#         'cart_products': p,
#         'sum_cart': sum([i.price for i in p]),
#         'teams': Team.objects.all(),
#     }
#     return render(request, 'service.html', context)


# class show service

class Service(ListView):
    model = Category
    template_name = 'service.html'
    context_object_name = 'categories_show'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update({
            'title': 'Service',
            'service': 'active',
            'categories_show': Category.objects.all(),
        })
        if self.request.user.is_authenticated:
            user = MyUser.objects.get(name=self.request.user.username)
            context.update({
                'count_cart': user.cart.count(),
                'cart_products': user.cart.all(),
                'sum_cart': sum([i.price for i in user.cart.all()]),
            })
        return context

    def post(self, request):
        return shopfind(request, request.POST['mainsearch'])


# func show contact
# def contact(request):
#     context = {
#         'title': 'Contact',
#         'contact': 'active',
#         'categories_show': Category.objects.all(),
#         'count_cart': len(p),
#         'cart_products': p,
#         'sum_cart': sum([i.price for i in p]),
#     }
#     return render(request, 'contact-us.html', context)


# class show contact

class Contact(ListView):
    model = Category
    template_name = 'contact-us.html'
    context_object_name = 'categories_show'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update({
            'title': 'Contact',
            'contact': 'active',
            'categories_show': Category.objects.all(),
        })
        if self.request.user.is_authenticated:
            user = MyUser.objects.get(name=self.request.user.username)
            context.update({
                'count_cart': user.cart.count(),
                'cart_products': user.cart.all(),
                'sum_cart': sum([i.price for i in user.cart.all()]),
            })
        return context

    def post(self, request):
        return shopfind(request, request.POST['mainsearch'])
