from django.conf.urls import patterns, include, url

from django.contrib import admin
from controllers.index import *
from controllers.product import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^product/\w+/$',product),
)
