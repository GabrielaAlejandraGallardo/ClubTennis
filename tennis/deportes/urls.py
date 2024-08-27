from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('deportes/nosotros',views.nosotros,name='nosotros'),
    path('deportes/listaD',views.listaD,name='listaD'),
    path('deportes/crear_editarDeporteD/<int:idDeporte>/', views.crear_editarDeporteD, name='crear_editarDeporteD'),
    path('deportes/eliminar/<int:idDeporte>',views.eliminar,name='eliminar'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)