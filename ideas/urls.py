from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from ideas import views

urlpatterns = patterns('',
    url(r'^$', views.IdeaList.as_view(), name='idea-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.IdeaDetail.as_view(), name='idea-detail'),
    # url(r'^comments/$', views.IdeaCommentList.as_view(), name='ideaComment-list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.IdeaCommentDetail.as_view(), name='ideaComment-detail'),
    url(r'^(?P<pk>[0-9]+)/add_comment/$', views.AddComment.as_view(), name='comment-on-idea'),
)


urlpatterns = format_suffix_patterns(urlpatterns)
