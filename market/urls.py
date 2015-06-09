from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from market import views

urlpatterns = patterns('',
    url(r'^$', views.AppList.as_view(), name='app-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.AppDetail.as_view(), name='app-detail'),
    url(r'^(?P<pk>[0-9]+)/rate/$', views.Rate.as_view(), name='rate-app'),
    url(r'^(?P<pk>[0-9]+)/add_comment/$', views.AddComment.as_view(), name='comment-on-app'),
)


urlpatterns = format_suffix_patterns(urlpatterns)
