from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from unclear import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.UnclearCreate.as_view(), name='create'),
    # url(r'^list/?$', views.UnclearList.as_view(), name='list'),
    url(r'^(?P<slug>.+)/$', csrf_exempt(views.UnclearDetail.as_view()), name='unclear_display'),
    url(r'^created/(?P<slug>.+)$', views.UnclearThanks.as_view(), name='unclear_thanks'),
)
