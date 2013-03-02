from django.conf.urls import patterns, include, url


urlpatterns = patterns('critics.views',
	url(r'^registro/$', 'createCritic', name='critic'),
    url(r'^login/$', 'loginrequest', name='login'),
    url(r'^logout/$', 'logutrequest', name='logout'),
    url(r'^perfil/$', 'verperfil', name='perfil'),
)
