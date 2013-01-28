from django.conf.urls import patterns, include, url


urlpatterns = patterns('main.views',
	url(r'^$', 'index', name='index'),
    url(r'^peliculas/$', 'peliculasView', name='peliculas'),
	url(r'^peliculas/(?P<nombrepeli>\w{0,50})/$', 'peliView', name='peliView'),
	url(r'^usuarios/', 'user', name='user'),

)
