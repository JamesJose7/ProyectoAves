from django.conf.urls import patterns, url

from appAves import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'', views.listado_aves, name='listado_aves'),
    # url(r'ave/(?P<id>\d+)$', views.materia, name='ave'),

)
