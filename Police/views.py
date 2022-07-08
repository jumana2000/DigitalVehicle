from turtle import end_fill
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *
from AdminDashboard.models import *
from Insurance.models import *
from WebApp.models import *
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

def s_rc_detail(request):
    if request.method == "POST":
        r_no = request.POST.get('r_no')
        rc = RC_Details.objects.filter(registration_no=r_no)
    return render(request,'s_rc_detail.html',{'data':rc})

def s_dl_details(request):
    if request.method == "POST":
        l_no = request.POST.get('l_no')
        dl = License_Details.objects.filter(dl_no=l_no)
    return render(request,'s_dl_details.html',{'data':dl})

def d_action(request):
    dl_id =request.POST.get('id')
    data = Dis_Action.objects.filter(dlid=dl_id,status=0)
    return render(request,'disciplinary_action.html',{'dl_id':dl_id,'data':data})

def disciplinary_action(request):
    if request.method == "POST":
        reason = request.POST.get('reason')
        amount = request.POST.get('amount')
        id = request.POST.get('id')
        data = Dis_Action(reason=reason,amount=amount,dlid=License_Details.objects.get(id=id),status=0)
        data.save()
    return HttpResponse("Punishment Update")

def fine_status(request,id):
    Dis_Action.objects.filter(id=id).update(status=1)
    return redirect('d_action')


def view_insurance(request):
    data = Insurance_DB.objects.all()
    return render(request,'view_insurance.html',{'data':data})

def complaints(request):
    data = Complaint.objects.all()
    return render(request,'complaints.html',{'data':data})

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

