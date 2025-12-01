from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import JsonResponse
from django.utils.html import escape

# Create your views here.

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def doctor_dash(request):
    return render(request,'doctor_dash.html')

def patient_dash(request):
    return render(request,'patient_dash.html')

def find_doctor(request):
    return render(request,'find_doctors.html')