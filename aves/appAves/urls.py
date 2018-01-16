from django.conf.urls import patterns, url

from appAves import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'listado/', views.listado_aves, name='listado_aves'),
    url(r'ave/(?P<id>\d+)$', views.ave, name='ave'),
    url(r'mapa/', views.mapa_view, name='mapa'),


)
