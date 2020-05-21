import logging
import os
from .base import *


logger = logging.getLogger(__file__)
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

SECRET_KEY = os.environ.get('SECRET_KEY', '')

ADMINS = (
    (
        os.environ.get('ADMIN_EMAIL_NAME', ''),
        os.environ.get('ADMIN_EMAIL_ADDRESS', ''),
    ),
)

STATIC_ROOT = os.path.join(BASE_DIR, os.environ.get('STATIC_ROOT', 'static/'))
STATIC_URL = os.environ.get('STATIC_URL', STATIC_URL)

MEDIA_ROOT = os.path.join(BASE_DIR, os.environ.get('MEDIA_ROOT', 'media/'))
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

# For HTTPS use
# Force redirection from HTTP to HTTPS, I'm sure you're doing this on NGINX
# SECURE_SSL_REDIRECT = True
# Encrypt session cookie (sends only with HTTPS)
# SESSION_COOKIE_SECURE = True
# Encrypt CSRF cookie (sends only with HTTPS)
# CSRF_COOKIE_SECURE = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'DB_ENGINE', 'django.db.backends.postgresql_psycopg2'
        ),
        'NAME': os.environ.get('SQL_DATABASE', 'postgres'),
        'USER': os.environ.get('SQL_USER', 'postgres'),
        'HOST': os.environ.get('SQL_HOST', 'postgres'),
        'PORT': os.environ.get('SQL_PORT', 5432),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'postgres'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'}
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(module)s '
            '(%(filename)s %(lineno)d): %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] (%(filename)s %(lineno)d): %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 1024*1024*5, # 5MB
            'backupCount': 3,
            'filename': os.path.join(
                os.path.dirname(BASE_DIR), 'logs', 'django.log'
            ),  # './logs/django.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'auth': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
