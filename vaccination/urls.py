from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parent/dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('parent/book-appointment/', views.book_appointment, name='book_appointment'),
]