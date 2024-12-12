from django.contrib import admin
from .models import Hospital, Parent, Child, Appointment

# Register your models here.

admin.site.register(Hospital)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Appointment)