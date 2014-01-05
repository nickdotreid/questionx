from django.conf.urls import patterns, include, url

urlpatterns = patterns('smsmessages.views',
	url(r'^$','recieve'),
	url(r'^(?P<phone_number>\+\w+)','send'),
	url(r'^(?P<phone_number>\+\w+)','list'),
)

import receivers