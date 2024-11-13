from socket import fromshare
from django import forms 
from .models import DeporteD, Categoria,D

class DeporteDForm(forms.ModelForm):
  class Meta:
        model=DeporteD
       #fields='__all__'
                         
        fields=('iddescripciondeporte','idCategoria','horario')
        labels ={
            "iddescripciondeporte" : "Nombre de deporte" ,
            'idCategoria': 'Código de Categoria:',
            "horario" : "Horario" ,
                  
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(DeporteDForm,self).__init__(*args,**kwargs)
        self.fields['iddescripciondeporte'].empty_label="Selecciona"
        self.fields['idCategoria'].required=True
        self.fields['horario'].required=False

class CategoriaForm(forms.ModelForm):
  class Meta:
        model=Categoria
       #fields='__all__'
                         
        fields=('descripcion',)
        labels ={          
         
            "descripcion" : "Nombre categoria" ,
                  
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(CategoriaForm,self).__init__(*args,**kwargs)
        self.fields['descripcion'].empty_label="Selecciona"
       
      
      
      
      
class DForm(forms.ModelForm):
      class Meta:
        model=D
       #fields='__all__'
                         
        fields=('nombre',)
        labels ={          
         
            "nombre" : "Nombre deporte" ,
                  
                   
        
        }
        
    
def __init__(self, *args, **kwargs):
        super(CategoriaForm,self).__init__(*args,**kwargs)
        self.fields['nombre'].empty_label="Selecciona"
       
      
      
      
      
               