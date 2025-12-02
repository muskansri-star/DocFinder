from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import JsonResponse
from django.utils.html import escape
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomerUser,Doctor, Appointment
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        action = request.POST.get("action")

        # ---------------- SIGNUP ----------------
        if action == "signup":
            role = request.POST.get("role")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm = request.POST.get("confirm")

            if password != confirm:
                messages.error(request, "Passwords do not match!")
                return redirect("signup")

            if CustomerUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect("signup")

            user = CustomerUser.objects.create_user(
                email=email,
                password=password,
                role=role
            )

            messages.success(request, "Account created! Please login.")
            return redirect("signup")

        # ---------------- LOGIN ----------------
        elif action == "login":
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(request, email=email, password=password)

            if user:
               login(request, user)

    # ROLE‑BASED REDIRECTION
            if user.role == "doctor":
             return redirect("doctor_dash")
            else:
             return redirect("patient_dash")


        messages.error(request, "Invalid login credentials")
        return redirect("signup")

    return render(request, "signup.html")

def doctor_dash(request):

     doctor = Doctor.objects.get(id=1)  # temporary (change ID)

     appointments = Appointment.objects.filter(doctor=doctor)

     return render(request, "doctor_dash.html", {
        "doctor": doctor,
        "appointments": appointments
    })

def patient_dash(request):
    return render(request, "patient_dash.html")

def find_doctors(request):
    query = request.GET.get("query", "")

    doctors = Doctor.objects.filter(
        Q(name__icontains=query) |
        Q(speciality__icontains=query) |
        Q(location__icontains=query)
    )

    return render(request, "find_doctors.html", {"doctors": doctors})

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time")
        symptoms = request.POST.get("symptoms")

        Appointment.objects.create(
            patient=request.user,
            doctor=doctor,
            appointment_date=date,
            appointment_time=time,
            symptoms=symptoms
        )

        return redirect('patient_dash')   # or your success page

    return render(request, "book_appointment.html", {"doctor": doctor})
