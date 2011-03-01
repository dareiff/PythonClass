from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^TheReiffs/', include('TheReiffs.foo.urls')),
	# (r'^', 'Photos.views.family'),
	(r'^images/', 'django.views.static.server', {'document_root': 'media/images/'}),
	(r'^family/', 'Photos.views.family'),
	(r'^familya/(?P<Photos_familymembers_id>\d+)/$', 'Photos.views.familydetail'),
	(r'^photo/(?P<Photos_photos_id>\d+)/$', 'Photos.views.photodetail'),
	(r'^photos/', 'Photos.views.photos'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^upload/', 'Photos.views.upload'),
# Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
	(r'^', 'Photos.views.index'),
)
