from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from product.models import Product, Category

# User App
from user.forms import UserRegisterForm, UserLoginForm

p = []  # Products in Cart
wishlist_product = []


def wishlist_add(request, pk):
    global wishlist_product
    for wp in Product.objects.all():
        if wp.id == pk and wp not in wishlist_product:
            wishlist_product.append(wp)

    context = {
        'title': 'Wishlist',
        'wp': wishlist_product,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }

    return render(request, 'wishlist.html', context)


def wishlist_del(request, pk):
    global wishlist_product
    vrem = []
    for wp in wishlist_product:
        if wp.id != pk:
            vrem.append(wp)
    wishlist_product = vrem

    context = {
        'title': 'Wishlist',
        'wp': wishlist_product,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }

    return render(request, 'wishlist.html', context)


def cart(request):
    sum_product = sum([i.price for i in p])  # sum all products in Cart

    context = {
        'title': 'Cart',
        'products': p,
        'sum_pro': sum_product - 52,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }

    return render(request, 'cart.html', context)


def cart_add(request, id):
    global p

    wishlist_del(request, id)
    for pr in Product.objects.all():
        if pr.id == id and pr not in p:
            p.append(pr)
    sum_product = sum([i.price for i in p])  # sum all products in Cart
    context = {
        'title': 'Cart',
        'products': p,
        'sum_pro': sum_product - 52,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),

    }

    return render(request, 'cart.html', context)


def cart_dele(request, id):
    global p
    n = []
    for i in p:
        if i.id != id:
            n.append(i)
    p = n
    sum_product = 0
    for i in p:
        sum_product += i.price
    context = {
        'title': 'Cart',
        'products': p,
        'sum_pro': sum_product - 52,
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),

    }

    return render(request, 'cart.html', context)


def my_account(request):
    context = {
        'title': 'My Account',
        'categories_show': Category.objects.all(),
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }
    return render(request, 'my-account.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
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
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
        'user_form': user_form,
    }
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
        'buy_products': p,
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
        'form': form,

    }
    return render(request, 'login.html', context)


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


def checkout(request):
    sum_product = sum([i.price for i in p])  # sum all products in Cart
    context = {
        'title': 'Checkout',
        'categories_show': Category.objects.all(),
        'buy_products': p,
        'sum_pro': sum_product - 52,
        'count_cart': len(p),
        'cart_products': p,
        'sum_cart': sum([i.price for i in p]),
    }
    return render(request, 'checkout.html', context)

    user_form = UserRegisterForm()
    form = UserLoginForm()

    user_form = UserRegisterForm()
    context = {
        'user_form': user_form,
    }
    return render(request, 'register.html', context)

