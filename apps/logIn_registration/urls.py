from django.conf.urls import url
from . import views #this line is new! #imports views.py from current folder
urlpatterns=[
    url(r'^$', views.index),#this line has changed!,
    url(r'^process$', views.process),
    url(r'^clear$', views.friends),
    url(r'^(?P<id>\d+)/success$', views.success),
    url(r'^logOut$', views.logOut),
    url(r'^friends$', views.friends),
    url(r'^friends/add$', views.friends_add),
    url(r'^friends/remove$', views.friends_remove),
    url(r'^user/(?P<id>\d+)$', views.user_show),

]
  