from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('servicios/nosotros',views.nosotros,name='nosotros'),
    path('servicios/listaServicio',views.listaServicio,name='listaServicio'),
    path('servicios/crear_editarServicio/<int:idServicio>',views.crear_editarServicio,name='crear_editarServicio'),
    path('servicios/eliminarS/<int:idServicio>',views.eliminarS,name='eliminarS'),
    path('servicios/listaContratacion',views.listaContratacion,name='listaContratacion'),
    path('servicios/crear_editarContratacion/<int:idContratacion>',views.crear_editarContratacion,name='crear_editarContratacion'),
    path('servicios/eliminarContratacion/<int:idContratacion>/',views.eliminarContratacion,name='eliminarContratacion'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)