from django.conf.urls import patterns, url
from payment_sys import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^pay/(?P<pk>[0-9]+)/$', views.pay, name='pay'),
    )
