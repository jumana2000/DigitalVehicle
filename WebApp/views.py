from django.shortcuts import render,redirect
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
