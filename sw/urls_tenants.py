from django.conf.urls import patterns, url, include
from customers.views import TenantView
#from inventories.views import CreateInventoryView

urlpatterns = patterns('',
    #url(r'^$', TenantView.as_view(), name='index'),
    #url(r'^inventories/',  CreateInventoryView.as_view()),
    url(r'^' , include('inventories.urls')),

)
