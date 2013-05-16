from django.conf.urls import patterns, include, url
from unclear import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.UnclearCreate.as_view(), name='create'),
    url(r'^(?P<slug>.+)/$', views.UnclearDetail.as_view(), name='unclear_display'),
    url(r'^created/(?P<slug>.+)$', views.UnclearThanks.as_view(), name='unclear_thanks'),
)
