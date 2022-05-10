from math import ceil
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


def exportarDatos(request):

    dataContactos=Contacto.objects.all()

    cedulas=[c.cedula for c in dataContactos]
    nombres=[n.nombre for n in dataContactos]
    apellidos=[a.apellido for a in dataContactos]
    correos=[e.correo for e in dataContactos]

    print(cedulas, nombres, apellidos, correos)
    
    context={
        "dataContactos":dataContactos
    }
    

    # list1 = [10,20,30,40,50,60]
    # list2 = [40,30,20,10,0,-10]
    # col1 = "X"
    # col2 = "Y"
    data = pandas.DataFrame({"Cedula":cedulas, "Nombre":nombres, "Apellido":apellidos, "Correos":correos})
    data.to_excel('./media/dataContactos.xlsx', sheet_name='sheet1', index=False)


    return render(request, "./Contactos/index.html",context)