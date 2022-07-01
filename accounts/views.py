from django.shortcuts import render, redirect
from Core.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

import random
import string


def randomString(stringlength=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringlength))

code = randomString()


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        user = User

        context ={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'phone': phone,
            'password': password,
        }

        if password == password2:
            if user.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                if user.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already used')
                    return redirect('register')
                else:
                    if user.objects.filter(phone=phone).exists():
                        messages.error(request, 'Phone no  is already used')
                        return redirect('register')
                    else:
                        send_mail(
                            'Account Creation Confirmation',
                            'Hi '+ first_name + ' You Confirmation code is: ' +code,
                            'jumana.sp@irohub.com',
                            [email],
                            fail_silently=False
                        )
                        request.method = 'GET'
                        return render(request, 'confirmregister.html', context)
        else:
            messages.error(request,'passwords donot match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def confirmregister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmcode = request.POST['confirmcode']
        user = User
        context ={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'username': username,
            'phone': phone,
            'password': password,
        }
        if code == confirmcode:
            user = user.objects.create_user(username=username, email=email, password=password,  phone=phone, first_name=first_name, last_name=last_name)
            user.save()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Confirmation Code')
            return render(request, 'confirmregister.html', context)
    else:
        return redirect('register')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_u'] = username
            request.session['password_u'] = password
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def userlogout(request):
    del request.session['username_u']
    del request.session['password_u']
    logout(request)
    messages.success(request, "you are now logged out")
    return redirect('index')