from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Socio
from .forms import SocioForm

# Create your views here
def listaSocio(request):
    socio=Socio.objects.all()
    return render(request,"CrudSocio/listado.html",{'socio':socio})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarSocio(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=SocioForm()   
        else:
            Socioid=Socio.objects.get(pk=id)
            formulario=SocioForm(instance=Socioid)
        return render(request,'CrudSocio/Crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=SocioForm(request.POST or None, request.FILES or None)
        else:
            Socioid=Socio.objects.get(pk=id)
            formulario=SocioForm(request.POST or None, request.FILES or None ,instance=Socioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaSocio')
        
def eliminarS(request, id):
    bc=Socio.objects.get(pk=id)
    bc.delete()
    return redirect('listaSocio')
        