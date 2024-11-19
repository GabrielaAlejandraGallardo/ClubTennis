from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Profesor
from .forms import ProfesorForm


# Create your views here

def listaProfesores(request):
    profesores=Profesor.objects.all()
    return render(request,"CrudProfesores/listado.html",{'profesores':profesores})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarProfesores(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=ProfesorForm()   
        else:
            profesorid=Profesor.objects.get(id=id)
            formulario=ProfesorForm(instance=profesorid)
        return render(request,'CrudProfesores/Crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=ProfesorForm(request.POST or None, request.FILES or None)
        else:
            profesorid=Profesor.objects.get(id=id)
            formulario=ProfesorForm(request.POST or None, request.FILES or None ,instance=profesorid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaProfesores')
        
def eliminarP(request, id):
    bc=Profesor.objects.get(pk=id)
    bc.delete()
    return redirect('listaProfesores')
        