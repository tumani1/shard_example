# coding: utf-8

from django.conf.urls.defaults import *


urlpatterns = patterns('accounts.views',
    url(r'^$', 'index'),
)
