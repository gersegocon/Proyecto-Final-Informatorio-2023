from django.shortcuts import render
from app.noticias.models import Noticia
def Home(request):
    return render(request, 'home.html')

def Nosotros(request):
    return render(request, 'nosotros.html')

def Contacto(request):
    return render(request, 'contacto.html')

def ListarNoticiasHome(request):
    contexto = {}

    n = Noticia.objects.all().order_by('-fecha_publicacion')
    
    contexto['noticias'] = n[0:2]

    return render(request, 'home.html', contexto)

