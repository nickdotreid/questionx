import os
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='sqlite:////' + os.getcwd() + '/database.db')}

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'