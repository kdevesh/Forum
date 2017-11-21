from django.conf.urls import include, url
from django.contrib.auth import views
from boards import views
urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
]    