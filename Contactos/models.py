from django.db import models
from django.forms import CharField, EmailField

# Create your models here.
class Contacto:
    cedula=CharField()
    nombre=CharField()
    apellido=CharField()
    correo=EmailField()
