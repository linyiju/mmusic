import os

# https://github.com/kennethreitz/dj-database-url
import dj_database_url
# https://github.com/heroku/django-heroku
# Configure Django App for Heroku.
import django_heroku

django_heroku.settings(locals())

ALLOWED_HOSTS = ['*']

DEBUG = False

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Static asset configuration.
STATIC_ROOT = 'staticfiles'

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
