from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('neurovault.apps.main.urls', app_name="main")),
    url(r'^studies/', include('neurovault.apps.statmaps.urls', app_name="statmaps")),
    url(r'^accounts/', include('neurovault.apps.users.urls', app_name="users")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))