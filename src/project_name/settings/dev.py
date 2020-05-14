"""
Settings for dev environment
"""

import logging
import os

from .base import *  # pylint: disable=W0401, W0614


logger = logging.getLogger(__file__)
ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]


def show_toolbar(request):
    """
    Allow show debug toolbar when developer settings is in use
    """
    return True


DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': show_toolbar}

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
            ),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {'handlers': ['file'], 'level': 'INFO', 'propagate': True},
        'users': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# Con esta configuración seremos capaces de consultar el código SQL
# generado a través de cualquier consulta del ORM de Django
if os.environ.get('DEBUG_SQL', 'False') == 'True':
    DEBUG_SQL = {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
    LOGGING['loggers'].update(DEBUG_SQL)
