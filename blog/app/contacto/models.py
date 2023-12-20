from django.db import models

class Contacto(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
