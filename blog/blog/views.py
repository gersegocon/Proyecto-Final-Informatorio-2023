from django.shortcuts import render
from app.viajes.models import Viaje
def Home(request):
    return render(request, 'home.html')

def Nosotros(request):
    return render(request, 'nosotros.html')

def Contacto(request):
    return render(request, 'contacto.html')

def ListarViajesHome(request): #para que aparezcan noticias en pagina de inicio
    contexto = {}

    n = Viaje.objects.all().order_by('-fecha_publicacion')
    
    contexto['viajes'] = n[0:2]

    return render(request, 'home.html', contexto)

