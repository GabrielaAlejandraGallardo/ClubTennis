from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('socios/nosotros',views.nosotros,name='nosotros'),
    path('socios/listaSocio',views.listaSocio,name='listaSocio'),
    path('socios/crear_editarSocio/<int:id>/',views.crear_editarSocio,name='crear_editarSocio'),
    path('socios/eliminarS/<int:id>',views.eliminarS,name='eliminarS'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)