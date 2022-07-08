from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about,name='about'),
    path('search_rc',views.search_rc,name='search_rc'),
    path('search_dl',views.search_dl,name='search_dl'),
    path('my_rc_dashboard',views.my_rc_dashboard,name='my_rc_dashboard'),
    path('my_dl_dashboard',views.my_dl_dashboard,name='my_dl_dashboard'),
    path('check_rc',views.check_rc,name='check_rc'),
    path('check_dl',views.check_dl,name='check_dl'),
    path('submit_rc',views.submit_rc,name='submit_rc'),
    path('submit_dl',views.submit_dl,name='submit_dl'),
    path('report',views.report,name='report'),
    path('report_data',views.report_data,name='report_data')
]