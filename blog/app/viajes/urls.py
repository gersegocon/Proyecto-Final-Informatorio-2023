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
     path('mis_favoritos', views.mis_favoritos, name='mis_favoritos'),
     path('viajes/<int:pk>/editar', views.EditarViajes, name='edit_viaje'),
     #path('editar_error', views.editar_error, name='editar_error'),
     path('crear_categoria/', views.CrearCategoria, name='crear_categoria'),
     path('comentario/add/<int:viaje_id>', views.AddComentario, name='add_comentario'),
     path('comentario/delete/<int:comentario_id>', views.BorrarComentario, name='delete_comentario'),
     path('comentario/edit/<int:comentario_id>', views.EditarComentario, name='edit_comentario'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
