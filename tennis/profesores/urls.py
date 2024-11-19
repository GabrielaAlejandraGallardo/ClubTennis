from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('profesores/nosotros',views.nosotros,name='nosotros'),
    path('profesores/listaProfesores',views.listaProfesores,name='listaProfesores'),
    path('profesores/<int:id>/',views.crear_editarProfesores,name='crear_editarProfesores'),
    path('profesores/eliminarP/<int:id>',views.eliminarP,name='eliminarP'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)