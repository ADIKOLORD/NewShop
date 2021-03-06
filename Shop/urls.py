"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static

from blog.views import blog, blogdetail
from . import settings
from main.views import About, Main, Service, Contact
from user.views import cart, \
    cart_add, cart_dele, checkout, \
    wishlist_add, wishlist_del, my_account, register, auth, logout_user
from product.views import shop, shopdetail

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', Main.as_view(), name='home'),
                  path('about/', About.as_view(), name='about'),
                  path('wishlist/<int:pk>', wishlist_add, name='wishlist'),
                  path('wishlistdel/<int:pk>', wishlist_del, name='wishlist_del'),
                  path('cart', cart, name='cart'),
                  path('cart_add/<int:id>', cart_add, name='cart_add'),
                  path('cart/delete/<int:id>', cart_dele, name='dele'),
                  path('shop/<int:pk>', shop, name='shop'),
                  path('shopdetail/<int:pk>', shopdetail, name='shopdetail'),
                  path('checkout', checkout, name='checkout'),
                  path('myaccount/', my_account, name='myaccount'),
                  path('service/', Service.as_view(), name='service'),
                  path('contact/', Contact.as_view(), name='contact'),
                  path('register/', register, name='register'),
                  path('login/', auth, name='login'),
                  path('logout/', logout_user, name='logout'),
                  path('blog', blog, name='blog'),
                  path('blog/<int:pk>', blogdetail, name='blogdetail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
