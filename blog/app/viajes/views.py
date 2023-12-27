from django.shortcuts import render, redirect, get_object_or_404
from .models import Viaje, Categoria, Comentario
from django.urls import reverse
from .forms import ViajeForm, CategoriaForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from app.usuarios.models import Favorito
from django.contrib import messages







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
    com = viaje.comentarios.all()

    # Verifica si el viaje está en favoritos del usuario
    if request.user.is_authenticated:
        is_favorito = Favorito.objects.filter(usuario=request.user, viaje=viaje).exists()
    
    # BORRAR VIAJE
    if request.method == 'POST' and 'delete_viaje' in request.POST:
        viaje.delete()
        return redirect('viajes:listar')
    
    # Comentarios
    if request.method == 'POST' and 'add_comentario' in request.POST:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            form.save()
            return redirect('viajes:detalle', pk=pk)
    else:
        form = ComentarioForm()

    # Obtener el viaje anterior y el siguiente
    viaje_anterior = Viaje.objects.filter(fecha_publicacion__lt=viaje.fecha_publicacion).order_by('-fecha_publicacion').first()
    siguiente_viaje = Viaje.objects.filter(fecha_publicacion__gt=viaje.fecha_publicacion).order_by('fecha_publicacion').first()

    contexto['viajes'] = viaje
    contexto['viaje_anterior'] = viaje_anterior
    contexto['siguiente_viaje'] = siguiente_viaje
    contexto['is_favorito'] = is_favorito  # Pasamos la información de favoritos al contexto
    contexto['comentarios'] = com

    return render(request, 'viajes/detalle.html', contexto)
    
@login_required
def AddViaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST or None, request.FILES) ##Request files es para las imagenes

        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.autor = request.user
            form.save()
            return redirect('viajes:listar')
    else:
        form = ViajeForm()
    
    if not request.user.is_staff:
        return  redirect('viajes:crear_error')
    
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


@login_required
def EditarViajes(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)

    if request.method == 'POST':
        form = ViajeForm(request.POST, request.FILES, instance = viaje)

        if form.is_valid():
            form.save()
            return redirect('viajes:detalle', pk = pk)
        else:
            form = ViajeForm(instance=viaje)
        
    # solo el autor puede editar la noticia
    if not request.user.is_staff:
        if viaje.autor != request.user:
            return  redirect('viajes:editar_error')
    return render(request, 'viajes/editar.html', {'form':form})

def editar_error(request):
    return render(request, 'viajes/editar_error.html')

def crear_error(request):
    return render(request, 'viajes/crear_error.html')

@login_required
def CrearCategoria(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)

        if categoria_form.is_valid():
            categoria_form.save()
            return redirect('viajes:listar')

    else:
        categoria_form = CategoriaForm()
    
    if not request.user.is_staff:
        return  redirect('viajes:crear_error')

    return render(request, 'viajes/crear_categoria.html', {'categoria_form': categoria_form})

@login_required
def AddComentario(request, viaje_id):

    viaje = get_object_or_404(Viaje, id = viaje_id)   
    if request.method == 'POST':
        
        contenido = request.POST.get("contenido")
        usuario = request.user.username
        # creacion de comentario
        Comentario.objects.create(viaje = viaje, usuario = usuario, contenido = contenido)
    
    return redirect('viajes:detalle', pk = viaje_id)


@login_required
def BorrarComentario(request, comentario_id):

    comentario = get_object_or_404(Comentario, id = comentario_id)   
    if comentario.usuario == request.user.username or request.user.is_staff:
        comentario.delete()
    
    return redirect('viajes:detalle', pk = comentario.viaje.pk)


@login_required
def EditarComentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    # Mensaje de error en caso de no ser el autor del comentario
    if not request.user.is_staff:
        if comentario.usuario != request.user.username:
            messages.error(request, 'No tenes permiso para editar este comentario')
            return redirect('viajes:detalle', pk=comentario.viaje.pk)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('viajes:detalle', pk=comentario.viaje.pk)
    else:
        form = ComentarioForm(instance=comentario)

    contexto = {
        'form':form,
        'comentario':comentario,
    }
    return render(request, 'viajes/editar_comentario.html', contexto)