from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password=None, role="patient"):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password, role="admin")
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomerUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("doctor", "Doctor"),
        ("patient", "Patient"),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomerUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    


class Appointment(models.Model):
 patient = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
 doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
 appointment_date = models.DateField()
 appointment_time = models.TimeField()
 symptoms = models.TextField(blank=True, null=True)
 created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.patient.email} → {self.doctor.name}"
