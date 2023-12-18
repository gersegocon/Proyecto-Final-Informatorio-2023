from django.shortcuts import render, redirect, get_object_or_404
from .models import Viaje, Categoria
from django.urls import reverse
from .forms import ViajeForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from app.usuarios.models import Favorito

# Create your views here.  


def ListarViajes(request):
    contexto = {}
    id_categoria = request.GET.get("id", None)

    if id_categoria:
        n = Viaje.objects.filter(categoria_viaje=id_categoria).order_by('-fecha_publicacion')
    else:
        n = Viaje.objects.all().order_by('-fecha_publicacion')
    
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        n = Viaje.objects.all().order_by('fecha_publicacion')

    antiguedad_des = request.GET.get("antiguedad_des")
    if antiguedad_des:
        n = Viaje.objects.all().order_by('-fecha_publicacion')

    
    orden_asc = request.GET.get("orden_asc")
    if orden_asc:
        n = Viaje.objects.all().order_by('titulo')

    orden_des = request.GET.get("orden_des")
    if orden_des:
        n = Viaje.objects.all().order_by('-titulo')

    cat = Categoria.objects.all().order_by('nombre')

    contexto['viajes'] = n
    contexto['categorias'] = cat

    return render(request, 'viajes/listar.html', contexto)

def DetalleViajes(request, pk):
    contexto = {}

    viaje = Viaje.objects.get(pk=pk)
    is_favorito = False

    # Verifica si el viaje está en favoritos del usuario
    if request.user.is_authenticated:
        is_favorito = Favorito.objects.filter(usuario=request.user, viaje=viaje).exists()
    
    # BORRAR VIAJE
    if request.method == 'POST' and 'delete_viaje' in request.POST:
        viaje.delete()
        return redirect('viajes:listar')

    # Obtener el viaje anterior y el siguiente
    viaje_anterior = Viaje.objects.filter(fecha_publicacion__lt=viaje.fecha_publicacion).order_by('-fecha_publicacion').first()
    siguiente_viaje = Viaje.objects.filter(fecha_publicacion__gt=viaje.fecha_publicacion).order_by('fecha_publicacion').first()

    contexto['viajes'] = viaje
    contexto['viaje_anterior'] = viaje_anterior
    contexto['siguiente_viaje'] = siguiente_viaje
    contexto['is_favorito'] = is_favorito  # Pasamos la información de favoritos al contexto

    return render(request, 'viajes/detalle.html', contexto)
    
@login_required
def AddViaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST or None, request.FILES) ##Request files es para las imagenes

        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.autor = request.user
            form.save()
            return redirect('home')
    else:
        form = ViajeForm()

    return render (request, 'viajes/addViaje.html', {'form':form})

@login_required
def toggle_favorito(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    usuario = request.user

    # Verifica si ya está guardado como favorito
    if usuario.favoritos().filter(viaje=viaje).exists():
        usuario.favoritos().get(viaje=viaje).delete()
        is_favorito = False
        message = "Eliminado de favoritos"
    else:
        Favorito.objects.create(usuario=usuario, viaje=viaje)
        is_favorito = True
        message = "Añadido a favoritos"

    return JsonResponse({'message': message, 'is_favorito': is_favorito})


@login_required
def mis_favoritos(request):
    viajes_favoritos = Viaje.objects.filter(favorito__usuario=request.user)
    return render(request, 'viajes/mis_favoritos.html', {'viajes_favoritos': viajes_favoritos})