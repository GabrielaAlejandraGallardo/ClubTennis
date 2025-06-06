from django.shortcuts import render, redirect, get_object_or_404
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import SociosCuota
from .forms import SocioCuotaForm


# Create your views here

def listaSocioCuota(request):
    socios_cuota=SociosCuota.objects.all()
    return render(request, 'CrudSocioCuota/listado.html', {'SociosCuota': socios_cuota})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

"""def crear_editarSocioCuota(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=SocioCuotaForm()   
        else:
            Socioid=SociosCuota.objects.get(pk=id)
            formulario=SocioCuotaForm(instance=Socioid)
        return render(request,'CrudSocioCuota/Crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=SocioCuotaForm(request.POST or None, request.FILES or None)
        else:
            Socioid=SociosCuota.objects.get(pk=id)
            formulario=SocioCuotaForm(request.POST or None, request.FILES or None ,instance=Socioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaSocioCuota')
    """
def crear_editarSocioCuota(request, id=0):
    if request.method == "GET":
        if id == 0:
            formulario = SocioCuotaForm()
        else:
            Socioid = get_object_or_404(SociosCuota, pk=id)
            formulario = SocioCuotaForm(instance=Socioid)
        return render(request, 'CrudSocioCuota/Crear.html', {'formulario': formulario})
    else:
        if id == 0:
            formulario = SocioCuotaForm(request.POST or None, request.FILES or None)
        else:
            Socioid = get_object_or_404(SociosCuota, pk=id)
            formulario = SocioCuotaForm(request.POST or None, request.FILES or None, instance=Socioid)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaSocioCuota')
def eliminarCuotaSocio(request, id):
    bsc=SociosCuota.objects.get(pk=id)
    bsc.delete()
    return redirect('listaSocioCuota')
        