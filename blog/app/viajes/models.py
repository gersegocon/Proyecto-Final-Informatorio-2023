from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Viaje(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    fecha_publicacion = models.DateTimeField('Data', auto_now_add=True)
    contenido = models.TextField('Texto')
    imagenes = models.ImageField(upload_to='viajes')
    categoria_viaje = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True)

    
    def __str__(self):
        return self.titulo


    