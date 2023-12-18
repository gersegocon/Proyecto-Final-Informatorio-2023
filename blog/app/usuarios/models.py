from django.db import models
from django.contrib.auth.models import AbstractUser
  # Ajusta el import según la ubicación correcta del modelo Viaje

# Create your models here.

#Crea usuarios
class Usuario(AbstractUser):
    def favoritos(self):
        return Favorito.objects.filter(usuario=self)
  

class Favorito(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    viaje = models.ForeignKey('viajes.Viaje', on_delete=models.CASCADE)
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} guardó {self.viaje.titulo}"
