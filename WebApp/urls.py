from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about,name='about'),
    path('search_rc',views.search_rc,name='search_rc')
]