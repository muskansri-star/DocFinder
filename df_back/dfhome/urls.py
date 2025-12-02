from django.contrib import admin
from django.urls import path
from dfhome import views
from . import views


urlpatterns = [
     path('', views.base, name='base'),
     path('home.html', views.home, name='home'),
     path('signup.html', views.signup, name='signup'),  
     path('doctor_dash.html',views.doctor_dash, name='doctor_dash'),  
     path('patient_dash.html',views.patient_dash, name='patient_dash'),
     path('find_doctors.html', views.find_doctors, name='find_doctors'),
]
