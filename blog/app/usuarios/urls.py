from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'usuarios'
urlpatterns = [
     path('login/', views.user_login, name='login'), #url para login
     path('logout/', views.user_logout, name='logout'), #url para logout
     path('registro/', views.Registro.as_view(), name='registro'), #url para el registro, distinto porque esta POO
     path('perfil/<int:pk>', views.Perfil, name='perfil'), #url para perfil de cualquier usuario
     path('mi-perfil/', views.MiPerfil, name='mi-perfil'), #url para perfil usuario propio
     path('usuarios/update-profile-picture/', views.actualizar_foto_perfil, name='update_profile_picture'),
     path('usuarios/update-profile-picture_users/<int:pk>/', views.actualizar_foto_perfil_users, name='update_profile_picture_users'),
     path('editar_foto_error', views.editar_foto_error, name='editar_foto_error'),
     path('usuarios/eliminar-foto/<int:pk>/', views.eliminar_foto_perfil, name='eliminar_foto_perfil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)