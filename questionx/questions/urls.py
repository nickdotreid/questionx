from django.conf.urls import patterns, include, url

urlpatterns = patterns('questions.views',
	url(r'^join','join'),
	url(r'^(?P<phone_number>\+\w+)/(?P<question_id>\d+)/delete','delete'),
	url(r'^(?P<phone_number>\+\w+)/(?P<question_id>\d+)','edit'),
	url(r'^(?P<phone_number>\+\w+)/create','create'),
	url(r'^(?P<phone_number>\+\w+)','view'),
)