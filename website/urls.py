from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'website.views.home', name='home'),
                       # url(r'^website/', include('website.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^tools/', include('rewriteengine.urls', namespace='rewriteengine')),
                       url(r'^search/', include('haystack.urls')),
                       url(r'^forum/', include('pybb.urls', namespace='pybb')),
                       url(r'^tinymce/', include('tinymce.urls')),
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^blogs/', include('blogs.urls', namespace="blogs")),
                       url(r'^', include('contents.urls', namespace="contents")),

                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='auth_login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
                       url(r'^accounts/register/$', 'blogs.views.register', name='registration_register'),


)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)