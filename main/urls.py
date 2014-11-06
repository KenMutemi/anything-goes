from django.conf.urls import patterns, url
from django.conf import settings
from main import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^summary/$', views.summary, name='summary'),
        url(r'^summaries/$', views.summaries, name='summaries'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
