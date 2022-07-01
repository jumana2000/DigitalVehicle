from django.urls import path 
from . import views

urlpatterns = [
    path('register/',views.register, name="register"),
    path('confirm/', views.confirmregister, name="confirmregister"),
    path('login/', views.userlogin, name="login"),
    
]