from django.conf.urls import patterns, url
from blogs import views

urlpatterns = patterns('',
                       url(r'^$', views.content, name="index"),
                       url(r'^(?P<page_slug>[\w-]+)/$', views.detail, name="detail"),
                       url(r'^category/(?P<page_slug>[\w-]+)/$', views.category, name="category"),

)