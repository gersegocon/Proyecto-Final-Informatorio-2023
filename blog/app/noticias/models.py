from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    fecha_publicacion = models.DateField('Data', auto_now_add=True)
    contenido = models.TextField('Texto')
    imagenes = models.ImageField(upload_to='noticias')
    categoria_noticia = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True)

    
    def __str__(self):
        return self.titulo


    