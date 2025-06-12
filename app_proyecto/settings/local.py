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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'diplomado067@gmail.com'
EMAIL_HOST_PASSWORD = 'amyq vcvp bian ydxu'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



STATIC_URL = 'static/'
