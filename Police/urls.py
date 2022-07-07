from django.urls import path
from . import views

urlpatterns = [
    path('police',views.police_index,name='police_index'),
    path('police_register',views.police_register,name='police_register'),
    path('pregister',views.pregister,name='pregister'),
    path('police_login',views.police_login,name='police_login'),
    path('plogin',views.plogin,name='plogin'),
    path('p_logout',views.p_logout,name='p_logout'),
    path('view_rc',views.view_rc,name='view_rc'),
    path('view_dl',views.view_dl,name='view_dl'),
    path('s_rc_detail',views.s_rc_detail,name='s_rc_detail'),
    path('s_dl_details',views.s_dl_details,name='s_dl_details'),
    path('view_insurance',views.view_insurance,name='view_insurance'),
    path('disciplinary_action',views.disciplinary_action,name='disciplinary_action'),
    path('d_action',views.d_action,name='d_action'),
    path('fine_status/<int:id>/',views.fine_status,name='fine_status')
]