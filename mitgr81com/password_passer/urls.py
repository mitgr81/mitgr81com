from django.conf.urls import patterns, include, url
from password_passer import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='password_passer'),
)
