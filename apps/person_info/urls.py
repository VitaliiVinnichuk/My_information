from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # index
                       url(r'^$',
                           'apps.person_info.views.index',
                           name='index'),
                       )
