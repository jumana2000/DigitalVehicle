from django.http import HttpResponse
from django.shortcuts import redirect, render
from AdminDashboard.models import *
from Insurance.models import Insurance_DB
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
    
    a = RC_Dashboard.objects.filter(userid=userid)
    print(a.values())

    if 'id' in request.session:
        for i in a:
            x = i.rid.insurance_expiry
    else:
        return render(request,'index.html')
    
    result1 = RC_Details.objects.filter(insurance_expiry=x)
    icount = RC_Details.objects.filter(insurance_expiry=x).count()
    # count = int(lcount)+int(icount)
    # print("Count : "+count)
    count = lcount+icount
    print(count)
    context = {'result1':result1,'result':result,'count':count}
    return render(request,'index.html',context)

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
  
def report(request):
    return render(request,'report.html')

def report_data(request):
    if request.method == "POST":
        date_reported = request.POST.get('date_reported')
        body_style = request.POST.get('body_style')
        color = request.POST.get('color')
        marker_plate_no = request.POST.get('marker_plate_no')
        vehicle_registered = request.POST.get('vehicle_registered')
        vehicle_register_state = request.POST.get('vehicle_register_state')
        door_locked = request.POST.get('door_locked')
        keys_in_vehicle = request.POST.get('keys_in_vehicle')
        # name_of_insurance_company = request.POST.get('name_of_insurance_company')
        owner_name = request.POST.get('owner_name')
        # phone = request.POST.get('phone')
        address = request.POST.get('address')
        court_available = request.POST.get('court_available')
        date_of_stolen = request.POST.get('date_of_stolen')
        time = request.POST.get('time')
        location_from = request.POST.get('location_from')
        data = Complaint(date_reported=date_reported,body_style=body_style,
        color=color,marker_plate_no=marker_plate_no,vehicle_registered=vehicle_registered,
        vehicle_register_state=vehicle_register_state,
        vehicle_identification_no=0,
        door_locked=door_locked,keys_in_vehicle=keys_in_vehicle,
        name_of_insurance_company='abc',
        owner_name=owner_name,phone=1234,address=address,
        court_available=court_available,date_of_stolen=date_of_stolen,
        time=time,location_from=location_from)
        data.save()
    return redirect('index')