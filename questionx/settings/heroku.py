import os

import dj_database_url
DATABASES = {'default':dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = False
if 'DEBUG' in os.environ:
	DEBUG = True
TEMPLATE_DEBUG = DEBUG

if False not in ( 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_STORAGE_BUCKET_NAME' in os.environ ):
	STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
	AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
	AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
	AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
	STATIC_URL = "https://{bucket_name}.s3.amazonaws.com/".format(
		bucket_name = AWS_STORAGE_BUCKET_NAME,
	)