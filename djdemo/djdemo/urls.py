from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from djdemo.views import profile

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djdemo.views.home', name='home'),
    # url(r'^djdemo/', include('djdemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/profile/$', profile),
)
