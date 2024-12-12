from django import forms
from django.contrib.auth.models import User
from .models import Parent, Child, Appointment

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['phone']

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'birth_date', 'vaccination_status']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['child', 'hospital', 'date']