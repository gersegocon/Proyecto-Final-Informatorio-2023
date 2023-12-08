from django.shortcuts import render, redirect
from .models import Viaje, Categoria
from django.urls import reverse
from .forms import ViajeForm
from django.contrib.auth.decorators import login_required

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

    n = Viaje.objects.get(pk=pk)

    #BORRAR VIAJE
    if request.method == 'POST' and 'delete_viaje' in request.POST:
        n.delete()
        return redirect('viajes:listar')
    # Obtener el viaje anterior y eñ siguiente
    viaje_anterior = Viaje.objects.filter(fecha_publicacion__lt=n.fecha_publicacion).order_by('-fecha_publicacion').first()
    siguiente_viaje = Viaje.objects.filter(fecha_publicacion__gt=n.fecha_publicacion).order_by('fecha_publicacion').first()

    contexto['viajes'] = n
    contexto['viaje_anterior'] = viaje_anterior
    contexto['siguiente_viaje'] = siguiente_viaje

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