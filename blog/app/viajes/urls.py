from django.urls import path
from . import views

app_name = 'viajes'
urlpatterns = [
     path('', views.Listarviajes, name='listar'),
     path('detalle/<int:pk>', views.Detalleviajes, name='detalle'),
     
]
