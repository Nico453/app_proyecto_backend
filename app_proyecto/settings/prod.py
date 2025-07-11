from .base import *
import os

DEBUG = os.getenv('DEBUG_PROD', 'False').lower() == 'true'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}


STATIC_URL = 'static/'
ROOT_URLCONF = 'app_proyecto.urls'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


