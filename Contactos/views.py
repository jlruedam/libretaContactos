from multiprocessing import context
from django.shortcuts import render
import pandas
from Contactos.models import Contacto

# Create your views here.

def index(request):
    dataContactos=Contacto.objects.all()
    print(dataContactos)
    context={
        "dataContactos":dataContactos
    }

    return render(request, "./Contactos/index.html",context)

def cargarDatos(request):
    data=request.FILES["dataExcel"]
    print("El archivo es:",data)
    df = pandas.read_excel(data)
    # print(list(df["Nombres"]))

    dataContactos=Contacto.objects.all()
    print(dataContactos)
    context={
        "dataContactos":dataContactos
    }


    for i in range(len(df)):
        # print(dict(df.iloc[i])["Cedula"])
        newContacto=Contacto(
            cedula=dict(df.iloc[i])["Cedula"],
            nombre=dict(df.iloc[i])["Nombres"],
            apellido=dict(df.iloc[i])["Apellidos"],
            correo=dict(df.iloc[i])["Correo"]
        )
        newContacto.save()
    
    return render(request, "./Contactos/index.html",context)