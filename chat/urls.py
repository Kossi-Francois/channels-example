from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^chat/$',  views.about, name='about'),
    url(r'^chat/new/$', views.new_room, name='new_room'),
    url(r'^chat/(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),

    url(r'^anotherApp/$', include("anotherApp.urls")),
]
