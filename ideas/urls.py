from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from ideas import views

urlpatterns = patterns('',
    url(r'^$', views.IdeaList.as_view(), name='idea-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.IdeaDetail.as_view(), name='idea-detail'),
)


urlpatterns = format_suffix_patterns(urlpatterns)
