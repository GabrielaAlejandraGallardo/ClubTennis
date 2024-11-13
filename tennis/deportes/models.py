from django.db import models


class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True,verbose_name="idCategoria")
    descripcion=models.CharField(verbose_name="descripcion",max_length=50)
    
    def __str__(self):
      fila=self.descripcion
      return fila
class D(models.Model):
    iddescripciondeporte=models.AutoField(primary_key=True,verbose_name="iddescripciondeporte")
    nombre=models.CharField(verbose_name="nombre",max_length=50)
    def __str__(self):
      fila=self.nombre
      return fila
        
# Create your models here.
class DeporteD(models.Model):
    idDeporte = models.AutoField(primary_key=True, db_column='idDeporte')
    iddescripciondeporte=models.ForeignKey(D,verbose_name="iddescripciondeporte",on_delete=models.CASCADE)
    idCategoria=models.ForeignKey(Categoria, verbose_name="idCategoria", on_delete=models.CASCADE)
    horario=models.FloatField(verbose_name="horario")
    
    
    def __str__(self):
        fila=str(self.idDeporte)+"-CÓDIGO CATEGORIA"+str(self.idCategoria)+"-codigo deporte"+str(self.iddescripciondeporte)
        return fila
    


    
















