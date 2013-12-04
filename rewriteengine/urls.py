from django.conf.urls import patterns, url
from rewriteengine import views

urlpatterns = patterns('',
                       url(r'^htaccess/$', views.htaccessrules, name="htaccess"),
                       url(r'^bulk-redirections/$', views.bulk_redirections, name="bulk-redirections"),
                       url(r'^sitemap-indexed/$', views.sitemap_indexed, name="googlesearch"),


)