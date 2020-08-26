from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("service", views.service, name='service'),
    path("contact",views.contact, name='contact')

    
]