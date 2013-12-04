from django.conf.urls import patterns, url

from contents import views

urlpatterns = patterns('',
                       url(r'^$', views.content, name='index'),
                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^(?P<page_slug>[\w-]+)/$', views.content, name='detail'),

)