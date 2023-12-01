from django.shortcuts import render
from .models import Noticia
# Create your views here.
def ListarNoticias(request):
    contexto = {}

    
    n = Noticia.objects.all().order_by('-fecha_publicacion')
    
    contexto['noticias'] = n

    return render(request, 'noticias/listar.html', contexto)

def DetalleNoticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk = pk)
    
    contexto['noticias'] = n

    return render(request, 'noticias/detalle.html', contexto)

