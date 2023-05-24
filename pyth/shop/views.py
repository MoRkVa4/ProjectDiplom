from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "pages/index.html", context)


def shop_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "pages/shop.html", context)


def about_view(request):
    return render(request, "pages/about.html")
