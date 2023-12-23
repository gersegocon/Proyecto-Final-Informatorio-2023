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
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)