from django.conf.urls import patterns, include, url
from django.contrib import admin
from console import urls as consoleUrl


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'virshsys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(consoleUrl)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)
