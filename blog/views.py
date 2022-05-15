from django.shortcuts import render, redirect

from blog.forms import CommentForm
from blog.models import Blog, Comment
from main.models import News
from product.models import Category, Product
from user.models import MyUser


def watch_blog(id):
    blog = Blog.objects.get(pk=id)
    blog.watch += 1
    blog.save()


def blog(request):
    context = {
        'title': 'Blog',
        'blog': 'active',
        'categories_show': Category.objects.all(),
        'news': News.objects.all(),
    }
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),
        })
    return render(request, 'blog.html', context)


def blogdetail(request, pk):
    watch_blog(pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.blog = Blog.objects.get(pk=pk)
            comment.save()
            return redirect('blogdetail', pk)

    context = {
        'title': 'BlogSingle',
        'blog': 'active',
        'categories_show': Category.objects.all(),
        'news': News.objects.all(),
        'one_blog': Blog.objects.get(pk=pk),
        'forms': CommentForm(),
        'comments': Comment.objects.all().filter(blog_id=pk),
    }
    if request.user.is_authenticated:
        user = MyUser.objects.get(name=request.user.username)
        context.update({
            'count_cart': user.cart.count(),
            'cart_products': user.cart.all(),
            'sum_cart': sum([i.price for i in user.cart.all()]),
        })

    return render(request, 'blog-single.html', context)
