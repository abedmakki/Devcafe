from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from project import views

urlpatterns = patterns('',
    url(r'^$', views.ProjectList.as_view(), name='project-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='project-detail'),
    url(r'^posts/$', views.PostList.as_view(), name='Post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='Post-detail'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='task-detail'),
    url(r'^(?P<pk>[0-9]+)/create_job/$', views.CreateJob.as_view(), name='create-job'),
    url(r'^assign_task/(?P<pk>[0-9]+)/$', views.AssignTask.as_view(), name='assign-task'),
    url(r'^applyjobs/(?P<pk>[0-9]+)/$', views.ApplyForJob.as_view(), name='apply-for-job'),
    url(r'^(?P<pk>[0-9]+)/view_requests/$', views.ViewRequests.as_view(), name='view-requests'),
    url(r'^resolve/(?P<pk>[0-9]+)/(?P<ans>[0-1])/$', views.ResolveRequests.as_view(), name='resolve-requests'),
    url(r'^(?P<pk>[0-9]+)/view_my_tasks/$', views.ViewMyTasks.as_view(), name='view-my-tasks'),
    url(r'^make_tasks_done/(?P<pk>[0-9]+)/$', views.MakeTaskDone.as_view(), name='update-task-done'),
    url(r'^changelogo/$', views.UploadProjectLogo.as_view(), name='project-change-logo'),
    url(r'^(?P<pk>[0-9]+)/quit/$', views.Quit.as_view(), name='quit'),
    url(r'^jobs/$', views.ViewJobs.as_view(), name='jobs'),
)


urlpatterns = format_suffix_patterns(urlpatterns)