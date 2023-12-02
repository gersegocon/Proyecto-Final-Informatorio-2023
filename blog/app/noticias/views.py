from django.shortcuts import render
from .models import Noticia, Categoria
# Create your views here.
def ListarNoticias(request):
    contexto = {}
    id_categoria = request.GET.get("id", None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia=id_categoria).order_by('-fecha_publicacion')
    else:
        n = Noticia.objects.all().order_by('-fecha_publicacion')
    
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        n = Noticia.objects.all().order_by('fecha_publicacion')

    antiguedad_des = request.GET.get("antiguedad_des")
    if antiguedad_des:
        n = Noticia.objects.all().order_by('-fecha_publicacion')

    
    orden_asc = request.GET.get("orden_asc")
    if orden_asc:
        n = Noticia.objects.all().order_by('titulo')

    orden_des = request.GET.get("orden_des")
    if orden_des:
        n = Noticia.objects.all().order_by('-titulo')

    cat = Categoria.objects.all().order_by('nombre')

    contexto['noticias'] = n
    contexto['categorias'] = cat

    return render(request, 'noticias/listar.html', contexto)

def DetalleNoticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)

    # Obtener la noticia anterior y la siguiente
    noticia_anterior = Noticia.objects.filter(fecha_publicacion__lt=n.fecha_publicacion).order_by('-fecha_publicacion').first()
    siguiente_noticia = Noticia.objects.filter(fecha_publicacion__gt=n.fecha_publicacion).order_by('fecha_publicacion').first()

    contexto['noticias'] = n
    contexto['noticia_anterior'] = noticia_anterior
    contexto['siguiente_noticia'] = siguiente_noticia

    return render(request, 'noticias/detalle.html', contexto)
