from django.urls import path
from . import views

app_name = 'viajes'
urlpatterns = [
     path('', views.ListarViajes, name='listar'),
     path('detalle/<int:pk>', views.DetalleViajes, name='detalle'),
     
]
