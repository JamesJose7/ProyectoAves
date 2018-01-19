from django.conf.urls import patterns, url

from appAves import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'listado/', views.listado_aves, name='listado_aves'),
                       url(r'ave/(?P<id>\d+)$', views.ave, name='ave'),
                       url(r'mapa/', views.mapa_view, name='mapa'),
                       url(r'top/', views.top_autores, name='top_autores'),
                       url(r'about/', views.about_view, name='about'),
                       url(r'autor/(?P<id>\d+)$', views.autor, name='autor'),
                       url(r'top_autores_view/$', views.top_autores_view, name='top_autores_view'),
                       url(r'api/test-json/$', views.sacar_data, name='sacar_data'),
                       )
