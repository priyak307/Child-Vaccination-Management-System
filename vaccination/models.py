from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    vaccination_status = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return f"{self.child.name} - {self.date}"