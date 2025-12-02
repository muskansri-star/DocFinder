from django import forms
from .models import CustomerUser

class SignupForm(forms.ModelForm):
    confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomerUser
        fields = ["email", "role", "password"]
        widgets = {
            "password": forms.PasswordInput()
        }

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password") != cleaned.get("confirm"):
            self.add_error("confirm", "Passwords do not match")
        return cleaned
