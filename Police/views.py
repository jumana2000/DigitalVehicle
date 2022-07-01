from django.shortcuts import render,redirect
from . models import *
from AdminDashboard.models import *
from Insurance.models import *
# Create your views here.

def police_index(request):
    result = RC_Details.objects.all()
    dl = License_Details.objects.all()
    return render(request,'police_index.html',{'data':result,'dl':dl})

def view_rc(request):
    data = RC_Details.objects.all()
    return render(request,'view_rc.html',{'data':data})

def view_dl(request):
    data = License_Details.objects.all()
    return render(request,'view_dl.html',{'data':data})

def view_insurance(request):
    data = Insurance_DB.objects.all()
    return render(request,'view_insurance.html',{'data':data})

def police_register(request):
    return render(request,'police_register.html')

def pregister(request):
    if request.method == 'POST':
        username_p = request.POST.get('username')
        password_p = request.POST.get('password')
        data = Police(username=username_p,password=password_p)
        
        data.save()
    return redirect('police_login')

def police_login(request):
    return render(request,'police_login.html')

def plogin(request):
    username_p = request.POST.get('username')
    password_p = request.POST.get('password')
    if Police.objects.filter(username=username_p,password=password_p).exists():
        data = Police.objects.filter(username=username_p,password=password_p).values('id').first()
        request.session['username_p'] = username_p
        request.session['password_p'] = password_p
        request.session['pid'] = data['id']
        return redirect('police_index')
    else:
        return redirect('police_login')

def p_logout(request):
    del request.session['username_p']
    del request.session['password_p']
    del request.session['pid']
    return redirect('police_login')

