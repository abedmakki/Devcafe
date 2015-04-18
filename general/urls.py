from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from general import views

urlpatterns = patterns('',
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view(), name='tag-detail'),
    url(r'^tags/$', views.TagList.as_view(), name='tag-list'),
)


urlpatterns = format_suffix_patterns(urlpatterns)
