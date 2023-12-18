from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'viajes'
urlpatterns = [
     path('', views.ListarViajes, name='listar'),
     path('detalle/<int:pk>', views.DetalleViajes, name='detalle'),
     path('addViaje', views.AddViaje, name='addViaje'),
     path('toggle_favorito/<int:pk>/', views.toggle_favorito, name='toggle_favorito'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
