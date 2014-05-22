from django.conf.urls import patterns, include, url

urlpatterns = patterns('appointments.views',
	url(r'^create','create'),
)