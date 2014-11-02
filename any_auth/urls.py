from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'any_auth.views.home', name='signin_home'),
        )
