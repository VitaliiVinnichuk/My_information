from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # index
                       url(r'^$',
                           'apps.person_info.views.index',
                           name='index'),
                       url(r'^request_logger/$',
                           'apps.person_info.views.request_logger',
                           name='request_logger'),
                       url(r'^edit/$',
                           'apps.person_info.views.edit',
                           name='edit'),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': '/'}, name="logout")
                       )
