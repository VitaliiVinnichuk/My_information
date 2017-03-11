from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from fortytwo_test_task.settings import common as settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^',
                           include('apps.person_info.urls')),
                       url(r'^admin/',
                           include(admin.site.urls)),
                       )
urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
