from django.conf.urls import patterns, include, url

urlpatterns = patterns('appointments.views',
	url(r'^create','create'),
	url(r'^(?P<appointment_id>\d+)','detail'),
	url(r'^$','list'),
)