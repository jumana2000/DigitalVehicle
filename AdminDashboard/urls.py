
from django.urls import path
from . import views

urlpatterns = [
    path('add_rc_details',views.add_rc_details,name='add_rc_details'),
    path('rc_detail',views.rc_detail,name='rc_detail'),
    path('view_rc_details',views.view_rc_details,name='view_rc_details'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('admin_index',views.admin_index,name='admin_index'), 
    path('add_license_details',views.add_license_details,name='add_license_details'),
    path('view_license_details',views.view_license_details,name='view_license_details'),
    path('view_insurance_details',views.view_insurance_details,name='view_insurance_details'),
    path('dl_details',views.dl_details,name='dl_details'),
    path('adlogout',views.adlogout,name='adlogout'),
    path('search_rc_detail',views.search_rc_detail,name='search_rc_detail'),
    path('search_dl_details',views.search_dl_details,name='search_dl_details')

]