from django.shortcuts import render
from AdminDashboard.models import *

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
