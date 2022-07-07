from django.http import HttpResponse
from django.shortcuts import redirect, render
from AdminDashboard.models import *
from . models import *
from Police.models import *
from datetime import datetime
import functools
 


# Create your views here.

def index(request):
    now = datetime.now() # current date and time
    date = now.strftime("%Y-%m-%d")
    license_expiry =  License_Details.objects.filter(licence_validity=date).values_list('id')
    data = license_expiry[0]
    print(license_expiry)
    print(data)
    print("The original tuple : " + str(data))
    # Convert Tuple to integer
    # Using reduce() + lambda
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, data)
    print("Tuple to integer conversion : " + str(res))
    le = str(res)
    userid = request.session.get('id')
    result = DL.objects.filter(dlid=le,userid=userid)
    lcount = DL.objects.filter(dlid=le,userid=userid).count()
    print(result)
    return render(request,'index.html',{'result':result,'lcount':lcount})

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
    username = request.session.get('id')
    data = DL.objects.filter(userid=username)
    dlid = DL.objects.filter(userid=username).values('dlid')[0]['dlid']
    print(dlid)
    disc_action = Dis_Action.objects.filter(dlid=dlid,status=0)
    return render(request,'my_dl_dashboard.html',{'data':data,'disc_action':disc_action})

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
    return render(request,"check_dl.html",{'dlid':dlid})

def submit_dl(request):
    if request.method == "POST":
        username = request.session.get('username_u')
        
        dlid = request.POST.get('dlid')
        
        dob = request.POST.get('dob')
        
        if License_Details.objects.filter(dob=dob,id=dlid).exists():
            data = DL(dob=dob,dlid=License_Details.objects.get(id=dlid),userid=User.objects.get(username=username))
            data.save()
            return redirect('my_dl_dashboard')
        else:
            return HttpResponse("Failed")
  