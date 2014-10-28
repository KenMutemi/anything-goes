from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^summary/$', views.summary, name='summary'),
        url(r'^summaries/$', views.summaries, name='summaries'),
        )
