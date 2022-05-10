from django.conf import settings
from django.contrib import admin
from django.urls import path
from Contactos import views

from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name="index"),
    path('cargarDatos/', views.cargarDatos, name="cargarDatos"),
    path('exportarDatos/', views.exportarDatos, name="exportarDatos"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)