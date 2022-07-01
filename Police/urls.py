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
    path('view_insurance',views.view_insurance,name='view_insurance')
]