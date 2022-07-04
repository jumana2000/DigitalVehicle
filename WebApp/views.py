from django.http import HttpResponse
from django.shortcuts import redirect, render
from AdminDashboard.models import *
from django.contrib import messages
from . models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def search_rc(request):
    if request.method == "POST":
        rc = request.POST.get('rc')
        data = RC_Details.objects.filter(registration_no=rc)
    return render(request,'search_rc.html',{'data':data})

def search_dl(request):
    if request.method == "POST":
        dl = request.POST.get('dl')
        data = License_Details.objects.filter(dl_no=dl)
    return render(request,'search_dl.html',{'data':data})
    

def my_dl_dashboard(request):
    pass

def my_rc_dashboard(request):
    username = request.session.get('id')
    data = RC_Dashboard.objects.filter(userid=username)
    return render(request,'my_rc_dashboard.html',{'data':data})

def check_rc(request):
    if request.method == "POST":
        rid = request.POST.get('rid')
        print(rid)
    return render(request,"check_rc.html",{'rid':rid})

def submit_rc(request):
    if request.method == "POST":
        username = request.session.get('username_u')
        rid = request.POST.get('rid')
        engine_no = request.POST.get('engine_no')
        chassis_no = request.POST.get('chassis_no')
        if RC_Details.objects.filter(engine_no=engine_no,chassis_no=chassis_no).exists():
            data = RC_Dashboard(engine_no=engine_no,chassis_no=chassis_no,
            rid=RC_Details.objects.get(id=rid),userid=User.objects.get(username=username))
            data.save()
            return redirect('my_rc_dashboard')
        else:
            return HttpResponse("Failed")
        
    
def check_dl(request):
    if request.method == "POST":
        dlid = request.POST.get('dlid')
        print(dlid)
    return render(request,"check_dl.html",{'dlid':dlid})

def submit_dl(request):
    pass