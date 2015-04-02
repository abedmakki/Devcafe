from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from project import views

urlpatterns = patterns('',
    url(r'^$', views.ProjectList.as_view(), name='project-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='project-detail'),
)


urlpatterns = format_suffix_patterns(urlpatterns)