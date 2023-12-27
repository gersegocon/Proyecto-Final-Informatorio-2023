from django.db import models
from app.usuarios.models import Usuario

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Viaje(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    resumen = models.CharField('Resumen', max_length=200, null=True)
    fecha_publicacion = models.DateTimeField('Data', auto_now_add=True)
    contenido = models.TextField('Texto')
    imagenes = models.ImageField('Imágenes',upload_to='viajes')
    categoria_viaje = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True)
    descripcion_imagen = models.CharField('Descripción imagen', max_length=100, null=True)
    
    def default_autor():
        return Usuario.objects.get(is_superuser=True).pk
    
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=default_autor)
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.contenido
    