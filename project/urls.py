from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from project import views

urlpatterns = patterns('',
    url(r'^$', views.ProjectList.as_view(), name='project-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='project-detail'),
    url(r'^posts/$', views.PostList.as_view(), name='Post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='Post-detail'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='Task-detail'),
    url(r'^(?P<pk>[0-9]+)/request_for_job/$', views.RequestForJob.as_view(), name='request-for-job'),
    url(r'^(?P<pk>[0-9]+)/assign_task/(?P<cont>[0-9]+)/$', views.AssignTask.as_view(), name='assign-task'),
    url(r'^(?P<pk>[0-9]+)/(?P<jobID>[0-9]+)/$', views.ApplyForJob.as_view(), name='apply-for-job'),
    url(r'^(?P<pk>[0-9]+)/view_requests/$', views.ViewRequests.as_view(), name='view-requests'),
)


urlpatterns = format_suffix_patterns(urlpatterns)