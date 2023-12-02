from django.shortcuts import render
from app.viajes.models import viaje
def Home(request):
    return render(request, 'home.html')

def Nosotros(request):
    return render(request, 'nosotros.html')

def Contacto(request):
    return render(request, 'contacto.html')

def ListarviajesHome(request):
    contexto = {}

    n = viaje.objects.all().order_by('-fecha_publicacion')
    
    contexto['viajes'] = n[0:2]

    return render(request, 'home.html', contexto)

