from mmusic.settings.sharded import *

DEBUG = True

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS += ['django_extensions']
