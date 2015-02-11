__author__ = 'evanwu'
from musicool import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^album/(?P<album_id>[\w]+)/$', views.album, name='category'),
                       url(r'^spotify_ask_authorized/$', views.spotify_ask_authorized, name='spotify_ask_authorized'),
                       url(r'^spotify_login/', views.spotify_login, name='spotify_login'),
                       url(r'search_spotify', views.search_spotify, name='search_spotify')
                       )