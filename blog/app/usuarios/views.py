
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from .forms import RegistroForm, PerfilUsuarioForm
from django.urls import reverse_lazy
from .models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.


def Perfil(request, pk):
    contexto = {}
    usuario = Usuario.objects.get(pk=pk)
    contexto['usuarios'] = usuario
    return render(request, 'usuarios/perfil.html', contexto)

def MiPerfil(request):
    return render(request, 'usuarios/mi-perfil.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') #redireccion a la pag de home post login
        else:
            messages.error(request, 'Usuario o contraseña invalido, intente de nuevo.')
    
    return render(request, 'usuarios/login.html')

def user_logout(request):
    logout(request)
    return redirect('usuarios:login')

# registro de usuarios
class Registro(CreateView):
    # formulario de django
    form_class = RegistroForm
    success_url = reverse_lazy('usuarios:login')
    template_name = 'usuarios/registro.html'

@login_required
def actualizar_foto_perfil(request):
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('usuarios:mi-perfil')  # Redirige a la página de perfil después de la actualización
    else:
        form = PerfilUsuarioForm(instance=request.user)

    return render(request, 'usuarios/update_profile_picture.html', {'form': form})

@login_required
def actualizar_foto_perfil_users(request, pk):
    
    usuario = Usuario.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil', pk=usuario.pk)  # Redirige a la página del perfil después de la actualización
    else:
        form = PerfilUsuarioForm(instance=request.user)
    
    if not request.user.is_staff:
        return  redirect('usuarios:editar_foto_error')

    return render(request, 'usuarios/update_profile_picture_users.html', {'form': form, 'usuarios':usuario})

def editar_foto_error(request):
    return render(request, 'usuarios/editar_foto_error.html')