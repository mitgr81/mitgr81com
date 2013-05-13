from django.conf.urls import patterns, include, url
from unclear import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pass_id>.+)/$', views.get, name='get'),
)
