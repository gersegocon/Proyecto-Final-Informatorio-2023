from django import forms
from .models import Viaje, Categoria

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

