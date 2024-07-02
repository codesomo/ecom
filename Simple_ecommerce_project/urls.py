"""
URL configuration for Simple_ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from EcomApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    path('admin/', admin.site.urls),
    path('',views.index, name="homepage"),
    path('httpresponse/',views.httpresponse, name="httpresponse"),
    path('crud/',views.crud, name="crud"),
    path('add/',views.add, name="add"),
    path('add_handler/',views.add_handler, name="add_handler"),
    path('update/',views.update, name="update"),
    path('update_handler/',views.update_handler, name="update_handler"),
    path('delete/',views.delete_handler, name="delete"),
    path('item_details/',views.item_details, name="item_details"),
    path('cart_list/',views.cart_list, name="cart_list"),
    path('add_to_cart/',views.add_to_cart, name="item_details"),
    path('sign_up/',views.sign_up_form, name="sign_up"),
    path('login/',views.login_form, name="login"),
    path('sign_up_handler/',views.sign_up_handler, name="sign_up_handler"),
    path('login_handler/',views.login_handler, name="login_handler"),
    path('logout_handler/',views.logout_handler, name="logout_handler"),
    path('category_details/',views.category_details, name="category_details"),
    path('all_category/',views.all_category, name="all_category"),
    path('all_items/',views.all_items, name="all_items"),
    path('all_cart_items/',views.all_cart_items, name="all_cart_items"),
    path('delete_cart/',views.delete_cart, name="delete_cart"),
    path('shipping_address/',views.shipping_address, name="shipping_address"),
    path('add_shipping_address/',views.add_shipping_address, name="add_shipping_address"),
    path('search/',views.search, name="search"),
    path('payment_order_handler/',views.payment_order_handler, name="payment_order_handler"),
    path('all_order_list/',views.all_order_list, name="all_order_list"),

    
    #path('login/',views.loginHandler, name="login"),
]
