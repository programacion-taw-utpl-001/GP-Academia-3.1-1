from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Academia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #lo primero que lee sonlas urls del admin de DJANGO
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portal/', include('portal.urls')),
]
