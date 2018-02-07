from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from hylakAutoSerwis import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'hylakAutoSerwis.views.home', name='home'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
