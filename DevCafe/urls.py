from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DevCafe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'DevCafe.views.home', name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('userapp.urls')),
    url(r'^ideas/', include('ideas.urls')),
)


urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'DevCafe.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
