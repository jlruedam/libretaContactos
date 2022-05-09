from django.contrib import admin
from django.urls import path
from Contactos import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('cargarDatos/', views.cargarDatos, name="cargarDatos"),
]