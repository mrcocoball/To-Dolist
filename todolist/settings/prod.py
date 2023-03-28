from .base import *
from decouple import config

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todolist_database',
        'USER' : config('DJANGO_DATASOURCE_USERNAME'),
        'PASSWORD' : config('DJANGO_DATASOURCE_PASSWORD'),
        'HOST' : 'mysql',
        'PORT' : '3309'
    }
}

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join('/code/static/files/staticfiles/')
STATICFILES_DIRS = []
DEBUG = False