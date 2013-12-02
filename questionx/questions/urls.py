from django.conf.urls import patterns, include, url

urlpatterns = patterns('questions.views',
	url(r'^join','join'),
	url(r'^$','join'),
	url(r'^(?P<phone_number>\w+)','view'),
)