# coding: utf-8

from django.conf.urls.defaults import *

from apps import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Стартовая страница
    (r'^$', 'apps.views.index'),

    # Аккаунт
    url(r'^account/', include('apps.accounts.urls')),

    # Профиль
    url(r'^profile/', include('apps.user_profile.urls')),

    # Админка
    url(r'^admin/', include(admin.site.urls))
)


# For built-in server in debug mode
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
