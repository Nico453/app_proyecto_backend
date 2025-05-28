from .base import *
import os

# Convertir a booleano manualmente
DEBUG = os.getenv('DEBUG')

# Leer hosts como lista
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USERNAME'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

STATIC_URL = 'static/'
