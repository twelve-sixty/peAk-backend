from django.conf.urls import url
from django.urls import path, include
from .views import index, room


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', room, name='room'),
    path('chat/', room, name='chat'),
]
