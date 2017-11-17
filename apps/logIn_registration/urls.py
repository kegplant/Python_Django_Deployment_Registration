from django.conf.urls import url
from . import views #this line is new! #imports views.py from current folder
urlpatterns=[
    url(r'^$', views.index),#this line has changed!,
    url(r'^process$', views.process),
    url(r'^clear$', views.clear),
    url(r'^(?P<id>\d+)/success$', views.success),
    url(r'^logOut$', views.logOut),
]
