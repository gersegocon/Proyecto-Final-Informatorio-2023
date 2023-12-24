from .base import *

DEBUG = False

ALLOWED_HOSTS = ['Viajazos.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Viajazos$default',
        'USER': 'Viajazos',
        'PASSWORD': 'rootroot',
        'HOST': 'Viajazos.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}