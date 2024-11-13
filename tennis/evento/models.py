from django.db import models
#from jugadores.models import Jugador

class Organizador(models.Model):
    idOrganizador=models.AutoField(primary_key=True,verbose_name="idOrganizador",db_column='idOrganizador')
    nom=models.CharField(max_length=45,verbose_name="nombre")
    contacto=models.IntegerField(verbose_name="contacto")
    
    def __str__(self):
        fila=str(self.idOrganizador)+"-Nombre Organizador: "+self.nom+"-Contacto: "+str(self.contacto)
        return fila
    
        
class Evento(models.Model):
    idEvento=models.AutoField(primary_key=True,verbose_name="idEvento",db_column='idEvento')
    nom= models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fecha=models.DateField(verbose_name="Fecha de Evento")
    ubicacion=models.CharField(max_length=20,verbose_name="Ubicacion")
    idOrganizador=models.ForeignKey(Organizador,verbose_name="idOrganizador", on_delete=models.CASCADE)
    
    def __str__(self):
        fila=str(self.idEvento)+"-"+self.nom+""+str(self.idOrganizador)
        return fila
    
    
    
    
    
    
