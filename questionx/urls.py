from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'questionx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('smsmessages.urls')),
    url(r'^appointments/', include('appointments.urls')),
    url(r'^', include('questions.urls')),
    url(r'^', 'front_page.views.signup'),
)
