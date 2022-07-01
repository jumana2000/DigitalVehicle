from django.urls import path
from . import views

urlpatterns = [
    path('i_register',views.i_register,name='i_register'),
    path('insurance_details',views.insurance_details,name='insurance_details'),
    path('insurance_data',views.insurance_data,name='insurance_data'),
    path('view_insurance_details',views.view_insurance_details,name='view_insurance_details'),
    path('insurance_register',views.insurance_register,name='insurance_register'),
    path('insurance_login',views.insurance_login,name='insurance_login'), 
    path('i_login',views.i_login,name='i_login')   
]
