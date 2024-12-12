from django.shortcuts import render, redirect
from .models import Hospital, Parent, Child, Appointment
from .forms import ParentForm, ChildForm, AppointmentForm

# Create your views here.
def home(request):
    return render(request, 'vaccination/home.html')

def parent_dashboard(request):
    parent = Parent.objects.get(user=request.user)
    children = Child.objects.filter(parent=parent)
    appointments = Appointment.objects.filter(child__in=children)
    return render(request, 'vaccination/parent_dashboard.html', {'children': children, 'appointments': appointments})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parent_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'vaccination/book_appointment.html', {'form': form})