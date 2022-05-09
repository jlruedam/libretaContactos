from django.shortcuts import render
import pandas

# Create your views here.

def index(request):
    return render(request, "./Contactos/index.html")

def cargarDatos(request):
    data=request.FILES["dataExcel"]
    print(data)
    df = pandas.read_excel(data, index_col="Identificador")
    print(df)

    # for data in df.columns[0]:
    #     print(data)

    return render(request, "./Contactos/index.html")