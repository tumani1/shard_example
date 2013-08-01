# coding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('user_profile.views',
    url(r'^$', 'index'),
    url(r'^shard/(?P<name>.*)/$', 'get_shard_values'),
)
