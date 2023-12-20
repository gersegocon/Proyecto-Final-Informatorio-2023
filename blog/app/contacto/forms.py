from django import forms
from .models import Contacto

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['email', 'nombre', 'telefono', 'mensaje']
