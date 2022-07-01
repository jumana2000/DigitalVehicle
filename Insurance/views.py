from click import password_option
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *


def insurance_details(request):
    return render(request,'insurance_details.html')

def insurance_data(request):
    if request.method == 'POST':
        period_from = request.POST['period_from']
        period_to = request.POST['period_to']
        engine_no = request.POST['engine_no']
        chassis_no = request.POST['chassis_no']
        reg_no = request.POST['reg_no']
        owner_name  = request.POST['owner_name']
        data = Insurance_DB(period_from=period_from,period_to=period_to,engine_no=engine_no,chassis_no=chassis_no,
                            registration_no=reg_no,owner_name=owner_name)
        data.save()
    return redirect('insurance_details')

def view_insurance_details(request):
    data = Insurance_DB.objects.all()
    return render(request,'view_insurance_details.html',{'data':data})

def insurance_register(request):
    return render(request,'insurance_register.html')

def i_register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = I_Register(email=email,password=password)
        data.save()
    return redirect('insurance_login')

def insurance_login(request):
    return render(request,'insurance_login.html')

def i_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if I_Register.objects.filter(email=email,password=password).exists():
            return render(request,'insurance_details.html')
        else:
            return redirect('i_login')




