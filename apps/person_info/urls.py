from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # index
                       url(r'^$',
                           'apps.person_info.views.index',
                           name='index'),
                       url(r'^request_logger/$',
                           'apps.person_info.views.request_logger',
                           name='request_logger'),
                       )
