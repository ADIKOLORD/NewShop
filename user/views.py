from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from product.models import Product, Category

# User App
from user.forms import UserRegisterForm, UserLoginForm
from user.models import MyUser


def wishlist_add(request, pk):
    # request.user.username
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        if int(pk) != 0:
            product = Product.objects.get(pk=pk)
            user.wishlist.add(product)
    else:
        return HttpResponse('<h1><a href="/register">You must register</a></h1>')

    context = {
        'title': 'Wishlist',
        'wp': user.wishlist.all(),
        'categories_show': Category.objects.all(),
        'count_cart': user.cart.count(),
        'cart_products': user.cart.all(),
        'sum_cart': sum([i.price for i in user.cart.all()]),
    }

    return render(request, 'wishlist.html', context)


def wishlist_del(request, pk):
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        product = Product.objects.get(pk=pk)
        user.wishlist.remove(product)
    else:
        return HttpResponse('<h1><a href="/register">You must register</a></h1>')

    context = {
        'title': 'Wishlist',
        'wp': user.wishlist.all(),
        'categories_show': Category.objects.all(),
        'count_cart': user.cart.count(),
        'cart_products': user.cart.all(),
        'sum_cart': sum([i.price for i in user.cart.all()]),
    }

    return render(request, 'wishlist.html', context)


'''

'categories_show': Category.objects.all(),
        'count_cart': user.cart.count(),
        'cart_products': user.cart.all(),
        'sum_cart': sum([i.price for i in user.cart.all()]),




'''


def cart(request):
    context = {
        'title': 'Cart',
        'categories_show': Category.objects.all(),

    }

    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'wp': user.wishlist.all(),
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),
            'products': user.cart.all(),
            'sum_pro': sum([i.price for i in user.cart.all()]) - 52,

        })
    return render(request, 'cart.html', context)


def cart_add(request, id):
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        product = Product.objects.get(pk=id)
        user.cart.add(product)
        user.wishlist.remove(product)
    else:
        return HttpResponse('<h1><a href="/register">You must register</a></h1>')

    user = MyUser.objects.get(name=request.user.username)
    wishlist_del(request, id)
    context = {
        'title': 'Cart',
        'categories_show': Category.objects.all(),
        'count_cart': user.cart.count(),
        'cart_products': user.cart.all(),
        'sum_cart': sum([i.price for i in user.cart.all()]),
        'products': user.cart.all(),
        'sum_pro': sum([i.price for i in user.cart.all()]) - 52,

    }

    return render(request, 'cart.html', context)


def cart_dele(request, id):
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        product = Product.objects.get(pk=id)
        user.cart.remove(product)
    else:
        return HttpResponse('<h1><a href="/register">You must register</a></h1>')

    context = {
        'title': 'Cart',
        'categories_show': Category.objects.all(),
        'count_cart': user.cart.count(),
        'cart_products': user.cart.all(),
        'sum_cart': sum([i.price for i in user.cart.all()]),
        'products': user.cart.all(),
        'sum_pro': sum([i.price for i in user.cart.all()]) - 52,

    }

    return render(request, 'cart.html', context)


def my_account(request):
    context = {
        'title': 'My Account',
        'categories_show': Category.objects.all(),

    }

    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),

        })

    return render(request, 'my-account.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            MyUser.objects.create(name=new_user.username,
                                  email=new_user.email)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('home')

        else:
            return HttpResponse('''<h1>Password is not correct or User already exist</h1>
            <br>
            <a href="/register">Try again</a>''')
    user_form = UserRegisterForm()
    context = {
        'title': 'REGISTER',
        'categories_show': Category.objects.all(),
        'user_form': user_form,
    }

    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),

        })
    return render(request, 'register.html', context)


def auth(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')

        else:
            username = form.cleaned_data['username']
            raise forms.ValidationError(f'Wrong or No username:{username} or password')
    form = UserLoginForm()
    context = {
        'title': 'LOGIN',
        'categories_show': Category.objects.all(),
        'form': form,

    }
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),

        })
    return render(request, 'login.html', context)


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


def checkout(request):
    context = {
        'title': 'Checkout',
        'categories_show': Category.objects.all(),

    }

    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'categories_show': Category.objects.all(),
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),
            'buy_products': user.cart.all(),
            'sum_pro': sum([i.price for i in user.cart.all()]) - 52,

        })
    return render(request, 'checkout.html', context)
