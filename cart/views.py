from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.models import UserModel
from fitapp.models import Products
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def CartView(request, total=0, count=0):
    c_user = request.user
    cart_items = CartItem.objects.filter(user=c_user)
    for i in cart_items:
        total += (i.s_product.price * i.quantity)
        count += i.quantity
    return render(request, 'cart.html', {'ct': cart_items, 'tot': total, 'cn': count, })


def add_to_cart(request, prod_slug):
    if request.user.is_authenticated:
        c_user = request.user
        sel_prod = Products.objects.get(slug=prod_slug)
        try:
            cart_items = CartItem.objects.get(user=c_user, s_product=sel_prod)
            if cart_items.quantity < cart_items.s_product.stock:
                cart_items.quantity += 1
            cart_items.save()
        except CartItem.DoesNotExist:
            cart_items = CartItem.objects.create(user=c_user, s_product=sel_prod, quantity=1)
            cart_items.save()
        return redirect('cart')
    else:
        return redirect('login')


def update_cart(request, id):
    user = request.user
    prod = CartItem.objects.get(user=user, id=id)
    quan = request.GET.get('item-quan' + str(id))
    product_quan = prod.s_product.stock
    if product_quan >= int(quan):
        if int(quan) >= 1:
            prod.quantity = quan
            prod.save()
            messages.info(request, 'Changes saved')
        else:
            messages.info(request, 'Please enter a valid input')
    else:
        messages.info(request, 'Insufficient stock')

    return redirect('cart')


def delete_cart(request, id):
    user = request.user
    prod = CartItem.objects.get(user=user, id=id)
    prod.delete()
    return redirect('cart')


def place_order(request):
    user = request.user
    usermdl = UserModel.objects.get(user=user)
    cart = CartItem.objects.all().filter(user=user)
    total = 0
    for i in cart:
        total += (i.s_product.price * i.quantity)
    order = OrderTable(user=user, total_amount=total)
    order.save()
    for i in cart:
        order_det = OrderDetails(order=order, product=i.s_product.name, product_quantity=i.quantity,
                                 total_price=i.s_product.price * i.quantity)
        order_det.save()
        i.s_product.stock = i.s_product.stock - i.quantity
        i.s_product.save()
    cart.delete()
    messages.info(request, 'Order has been placed successfully')
    messages.info(request, 'Items will be shipped to ' + usermdl.address, usermdl.city)
    return redirect('/')
