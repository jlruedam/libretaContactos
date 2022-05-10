from django.db import models
from django.forms import CharField, EmailField

# Create your models here.
class Contacto(models.Model):
    cedula=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()



