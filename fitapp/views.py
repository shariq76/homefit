from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    featured = Products.objects.all().filter(featured=True)
    cat = Category.objects.all()
    return render(request, 'index.html', {'fr': featured, 'ct': cat})


def products(request, cat_slug=None):
    if cat_slug is None:
        prod = Products.objects.all().filter(available=True)
    else:
        cat = Category.objects.get(slug=cat_slug)
        prod = Products.objects.all().filter(category=cat)
    return render(request, 'products.html', {'pr': prod})


def selected1(request, cat_slug, prod_slug):
    cat = Category.objects.get(slug=cat_slug)
    prod = Products.objects.get(slug=prod_slug, category=cat)
    similiar_prod = Products.objects.all().filter(category=cat)
    return render(request, 'single-product.html', {'ct': cat, 'pr': prod, 'sm': similiar_prod})


def search(request):
    if 's_query' in request.GET:
        query = request.GET.get('s_query')
        if query.isspace() == True:
            messages.showinfo(request, 'Please enter a valid keyword')
            return redirect('/')
        else:
            prod = Products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
            return render(request, 'search.html', {'qr': query, 'pr': prod})


def about(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')
