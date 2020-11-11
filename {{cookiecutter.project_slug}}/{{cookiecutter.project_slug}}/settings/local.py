"""
Development settings and globals.
"""

from __future__ import absolute_import

from .common import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "{{cookiecutter.project_slug}}",
        'USER': "",
        'PASSWORD': "",
        'HOST': "",
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

INSTALLED_APPS += (
)

MIDDLEWARE_CLASSES += (
)

INTERNAL_IPS = ('127.0.0.1',)