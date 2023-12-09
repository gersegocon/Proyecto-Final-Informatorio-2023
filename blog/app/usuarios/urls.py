from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
     path('login/', views.user_login, name='login'), #url para login
     path('logout/', views.user_logout, name='logout'), #url para logout
     path('registro/', views.Registro.as_view(), name='registro'), #url para el registro, distinto porque esta POO
     path('perfil/', views.Perfil, name='perfil'), #url para perfil de cualquier usuario
     path('mi-perfil/', views.MiPerfil, name='mi-perfil'), #url para perfil usuario propio
]
