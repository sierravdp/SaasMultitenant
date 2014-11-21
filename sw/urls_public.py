from django.conf.urls import patterns
from sw.views import HomeView

urlpatterns = patterns('',
   (r'^$', HomeView.as_view()),
)
