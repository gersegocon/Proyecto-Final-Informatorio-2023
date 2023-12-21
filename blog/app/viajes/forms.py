from django import forms
from .models import Viaje, Categoria, Comentario

class ViajeForm(forms.ModelForm):

    class Meta:
        model = Viaje
        fields = [
            'titulo',
            'resumen',
            'contenido',
            'imagenes',
            'categoria_viaje',
        ]
        

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ComentarioForm(forms.ModelForm):
     
    class Meta:
        model = Comentario
        fields = [
            'contenido'
        ]
        exclude = ['usuario']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        
        super(ComentarioForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.usuario = user.username
