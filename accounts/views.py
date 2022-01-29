from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from cart.models import *
from .models import UserModel, FeedBack


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        user = authenticate(request, username=uname, password=pswd)
        if user is None:
            messages.info(request, 'Invalid credentials. Try again')
            return redirect('login')
        else:
            auth_login(request, user)
            return redirect('/')
    return render(request, 'accounts.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        uname = request.POST['uname']
        pswd1 = request.POST['pswd1']
        pswd2 = request.POST['pswd2']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        if pswd1 != pswd2:
            messages.info(request, 'Passwords do not match. Try again.')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists.')
                return redirect('register')
            else:
                if User.objects.filter(username=uname).exists():
                    messages.info(request, 'Username already taken.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=fname, last_name=lname, email=email, password=pswd1,
                                                    username=uname)
                    user.save()
                    user_model = UserModel(user=user, phone=phone, address=address, city=city, state=state,
                                           country=country)
                    user_model.save()
                    return redirect('/')
    else:
        return render(request, 'register.html')


def personal_info(request):
    user = request.user
    try:
        usermodel = UserModel.objects.get(user=user)
    except ObjectDoesNotExist:
        messages.info(request, 'Admin does not have a user model')
        return redirect('/')
    return render(request, 'personal_info.html', {'usr': user, 'usrmdl': usermodel})


def update_info(request):
    user = request.user
    usrmdl = UserModel.objects.get(user=user)
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['phone']
    username = request.POST['uname']
    if User.objects.filter(username=username).exists():
        if user.username == username:
            user.username = username
            user.first_name = fname
            user.last_name = lname
            user.email = email
            usrmdl.phone = phone
            user.save()
            usrmdl.save()
            messages.info(request, 'Changes saved')
        else:
            messages.info(request, 'Username already taken')
    else:
        user.username = username
        user.first_name = fname
        user.last_name = lname
        user.email = email
        usrmdl.phone = phone
        user.save()
        usrmdl.save()
        messages.info(request, 'Changes saved')
    return redirect('personal')


def address_info(request):
    user = request.user
    usermodel = UserModel.objects.get(user=user)
    return render(request, 'address_info.html', {'usr': user, 'usrmdl': usermodel})


def address_update(request):
    user = request.user
    usermodel = UserModel.objects.get(user=user)
    address = request.POST['addr']
    city = request.POST['city']
    if address == '' or city == '':
        messages.info(request, 'Please input a value')
    else:
        usermodel.address = address
        usermodel.city = city
        usermodel.save()
        messages.info(request, 'Changes saved')
    return redirect('address')


def orders(request):
    user = request.user
    orders = OrderTable.objects.all().filter(user=user)
    try:
        usermodel = UserModel.objects.get(user=user)
    except ObjectDoesNotExist:
        messages.info(request, 'Admin does not have a user model')
        return redirect('/')
    return render(request, 'orders.html', {'usr': user, 'usrmdl': usermodel, 'ord': orders})


def order_summary(request, order_id):
    order = OrderTable.objects.get(id=order_id)
    order_det = OrderDetails.objects.all().filter(order=order)
    return render(request, 'order_summary.html', {'ord': order, 'ord_det': order_det})


def feedBack(request):
    user = request.user
    name = request.POST['name']
    email = request.POST['email']
    feedback = request.POST['feedback']
    feed_back = FeedBack(user=user, name=name, email=email, feedback=feedback)
    feed_back.save()
    messages.info(request, 'Feedback sent successfully')
    return redirect('/')
