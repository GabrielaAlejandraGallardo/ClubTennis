from django.shortcuts import render, redirect, get_object_or_404
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import SociosCuota
from .forms import SocioCuotaForm
from collections import defaultdict
from socios.models import Socio  # Asegúrate de importar tu modelo Socio


def listaSocioCuota(request):
    socios_cuota = SociosCuota.objects.all().order_by('cuotaMes')
    pagos_por_mes = defaultdict(list)
    total_por_mes = defaultdict(float)

    for sc in socios_cuota:
        mes = sc.cuotaMes
        pagos_por_mes[mes].append(sc)
        total_por_mes[mes] += float(sc.importe)

    # Convertir a lista de tuplas para el template
    pagos_y_totales = [
        (mes, pagos_por_mes[mes], total_por_mes[mes])
        for mes in pagos_por_mes
    ]

    return render(request, 'CrudSocioCuota/listado.html', {
        'pagos_y_totales': pagos_y_totales,
    })
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
        return redirect('listaSocioCuota')\"\"\"sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        

def crear_editarSocioCuota(request, id=0):
    socios = Socio.objects.all()
    if request.method == "GET":
        if id == 0:
            formulario = SocioCuotaForm()
        else:
            Socioid = get_object_or_404(SociosCuota, pk=id)
            formulario = SocioCuotaForm(instance=Socioid)
        return render(request, 'CrudSocioCuota/Crear.html', {
            'formulario': formulario,
            'socios': socios,  # <-- pasa la lista de socios aquí
        })
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
    bsc = get_object_or_404(SociosCuota, pk=id)
    bsc.delete()
    return redirect('listaSocioCuota')