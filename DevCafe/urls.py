from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from DevCafe.views import IndexView
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns = patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'DevCafe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    (r'^accounts/', include('allauth.urls')),
    (r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('userapp.urls')),
    url(r'^ideas/', include('ideas.urls')),
    url(r'^projects/', include('project.urls')),
    url('^.*$', IndexView.as_view(), name='index'),
)


# if settings.DEBUG:
#     urlpatterns += patterns(
# (r'^media/(?P<path>.*)$',
#  'django.views.static.serve',
#  {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),)
