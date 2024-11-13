from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('sociosCuota/nosotros',views.nosotros,name='nosotros'),
    path('sociosCuota/listaSocioCuota',views.listaSocioCuota,name='listaSocioCuota'),
    path('sociosCuota/crear_editarSocioCuota/<int:id>/',views.crear_editarSocioCuota,name='crear_editarSocioCuota'),
    path('sociosCuota/eliminarCuotaSocio/<int:id>',views.eliminarCuotaSocio,name='eliminarCuotaSocio'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)