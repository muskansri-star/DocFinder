from django.contrib import admin

# Register your models here.

from .models import CustomerUser, Doctor,Appointment

"""
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ("email", "role", "is_active", "is_staff", "is_superuser")
    search_fields = ("email", "role")
    list_filter = ("role", "is_active", "is_staff")

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "speciality", "location", "contact")
    search_fields = ("name", "speciality", "location")    

admin.site.register(CustomerUser)

admin.site.register(Doctor) """

from django.contrib import admin
from .models import CustomerUser, Doctor

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ("email", "role", "is_active", "is_staff", "is_superuser")
    search_fields = ("email", "role")
    list_filter = ("role", "is_active", "is_staff")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "speciality", "location", "contact")
    search_fields = ("name", "speciality", "location")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "appointment_date", "appointment_time")
    search_fields = ("patient__email", "doctor__name")
    list_filter = ("appointment_date",)
