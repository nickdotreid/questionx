from django.conf.urls import patterns, include, url

urlpatterns = patterns('questions.views',
	url(r'^join','join'),
)