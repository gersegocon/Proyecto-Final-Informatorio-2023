from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.vista_contacto.as_view(), name='contacto')
]
