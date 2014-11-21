from django.conf.urls import patterns, url
from .views import Registrarse
from .views import Create
from .views import Delete
from .views import List
#from inventories import views

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'index_login.html'}, name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^registrarse/$', Registrarse.as_view(), name='registrarse'),
    url(r'^list', List.as_view(), name='list'),
    url(r'^create$', Create.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)$', Delete.as_view(), name='delete'),

)