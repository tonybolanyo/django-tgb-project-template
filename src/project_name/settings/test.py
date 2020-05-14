"""
Settings for testing environment
"""
from .base import *


INSTALLED_APPS += ['django_nose']

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--exe',
    '--verbosity=2',
    '--cover-erase',
    '--cover-html',
    '--cover-min-percentage=85',
    '--cover-package={{ project_name }},users',
    '--rednose',
    '--force-color',
    '--with-doctest',
    # '--with-coverage',
    # '--cover-config-file=.coveragerc',
]
