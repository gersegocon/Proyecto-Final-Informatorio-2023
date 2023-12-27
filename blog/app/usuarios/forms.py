from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

# Crea registro de usuarios
class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su email'}))
    first_name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(label='Apellido', required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))
    username = forms.CharField(label='Nombre de usuario', required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese username'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese contraseña'}), required=True)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Confirme contraseña'}), required=True)
    imagen = forms.ImageField(label='Imagen de perfil', required=False)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'imagen',
        ]

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['imagen']