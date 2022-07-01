from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from . models import *
from django.contrib import messages
from Insurance.models import *
# Create your views here.

def admin_index(request):
    result = RC_Details.objects.all()
    dl = License_Details.objects.all()
    return render(request,'admin_index.html',{'data':result,'dl':dl})

def add_rc_details(request):
    result = RC_Details.objects.all()
    return render(request,'add_rc_details.html',{'data':result})

def rc_detail(request):
    if request.method == "POST":
        owner_name = request.POST.get('owner_name')
        reg_rto = request.POST.get('reg_rto')
        maker_model = request.POST.get('maker_model')
        vehicle_class = request.POST.get('vehicle_class')
        fuel_norms = request.POST.get('fuel_norms')
        engine_no = request.POST.get('engine_no')
        chassis_no = request.POST.get('chassis_no')
        reg_date = request.POST.get('reg_date')
        fitness_upto = request.POST.get('fitness_upto')
        insurance_expiry = request.POST.get('insurance_expiry')
        insurance_expiry_in = request.POST.get('insurance_expiry_in')
        reg_no = request.POST.get('reg_no')
        color = request.POST.get('color')
        unloaded_weight = request.POST.get('unloaded_weight')
        data = RC_Details(owner_name=owner_name,registered_rto=reg_rto,maker_model=maker_model,
                          vehicle_class=vehicle_class,fuel_norms=fuel_norms,
                          engine_no=engine_no,chassis_no=chassis_no,registration_date=reg_date,
                          fitness_upto=fitness_upto,insurance_expiry=insurance_expiry,
                          insurance_expiry_in=insurance_expiry_in,registration_no=reg_no,
                          color=color,unloaded_weight=unloaded_weight)
        data.save()
    return redirect('add_rc_details')

def view_rc_details(request):
    data = RC_Details.objects.all()
    return render(request,'view_rc_details.html',{'data':data})

def add_license_details(request):
    return render(request,'add_license_details.html')

def dl_details(request):
    if request.method == 'POST':
        dl_no = request.POST.get('dl_no')
        holder_name = request.POST.get('holder_name')
        authority_code = request.POST.get('authority_code')
        license_authority = request.POST.get('license_authority')
        vehicle_class = request.POST.get('vehicle_class')
        issue_date = request.POST.get('issue_date')
        licence_validity = request.POST.get('licence_validity')
        data = License_Details(dl_no=dl_no,holder_name=holder_name,authority_code=authority_code,license_authority=license_authority,vehicle_class=vehicle_class,issue_date=issue_date,licence_validity=licence_validity)
        data.save()
    return redirect('view_license_details')
    
def view_license_details(request):
    data = License_Details.objects.all()
    return render(request,'view_license_details.html',{'data':data})

def view_insurance_details(request):
    data = Insurance_DB.objects.all()
    return render(request,'view_insurance_details.html',{'data':data})

def search_rc_detail(request):
    if request.method == "POST":
        r_no = request.POST.get('r_no')
        rc = RC_Details.objects.filter(registration_no=r_no)
    return render(request,'search_rc_detail.html',{'data':rc})

def search_dl_details(request):
    if request.method == "POST":
        l_no = request.POST.get('l_no')
        dl = License_Details.objects.filter(dl_no=l_no)
    return render(request,'search_dl_details.html',{'data':dl})

def admin_login(request):
    return render(request,'admin_login.html')

def adlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            messages.success(request, 'You are now logged in')
            return redirect('admin_index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('admin_login')
    else:
        return render(request, 'admin_login.html')

def adlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    return redirect('admin_login')