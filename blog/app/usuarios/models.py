from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import default_storage

  

#Crea usuarios
class Usuario(AbstractUser):
    def favoritos(self):
        return Favorito.objects.filter(usuario=self)
  #imagen de perfil de usuario
    imagen = models.ImageField('Imágenes', upload_to='usuarios')

    def eliminar_imagen_perfil(self):
        # Eliminar la imagen de perfil del almacenamiento
        if self.imagen:
            default_storage.delete(self.imagen.name)
            self.imagen = None
            self.save()

    # USUARIOS QUE TENEMOS EN NUESTRO BLOG Y SUS PERMISOS
    USUARIO_COLABORADOR = 'Colaborador'
    USUARIO_VISITANTE = 'Visitante'
    USUARIO_MIEMBRO = 'Miembro'
    USUARIO_SUPER = 'Superusuario'


    TIPOS_DE_USUARIO = [
        (USUARIO_COLABORADOR, 'Colaborador'), #is_superuser=False, is_staff=True
        (USUARIO_VISITANTE, 'Visitante'), #no es nada / no aparece en la base de datos
        (USUARIO_MIEMBRO, 'Miembro'), #is_superuser=False, is_staff=False
        (USUARIO_SUPER, 'Superusuario'), #is_superuser=True, is_staff=True
    ]
    #atributo que determina el tipo de usuario, por default es usuario_miembro (cuando te registras en el blog toma este)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_DE_USUARIO, default=USUARIO_MIEMBRO)


    def __str__(self):
        return self.username


# Señal para asignar el tipo de usuario "Superusuario" cuando se crea un superusuario
@receiver(post_save, sender=Usuario)
def asignar_tipo_usuario(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        instance.tipo_usuario = Usuario.USUARIO_SUPER
        instance.save()
        print(f"Usuario {instance.username} es un Superusuario.")


# Señal para asignar el tipo de usuario "Miembro" cuando se crea un usuario
@receiver(post_save, sender=Usuario)
def asignar_miembro(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        instance.tipo_usuario = Usuario.USUARIO_MIEMBRO
        instance.save()
        print(f"Usuario {instance.username} es un Miembro.")

class Favorito(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    viaje = models.ForeignKey('viajes.Viaje', on_delete=models.CASCADE)
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} guardó {self.viaje.titulo}"
