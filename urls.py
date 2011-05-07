from django.conf.urls.defaults import *

# import in order to access settings.py variables
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# importing all the views  
from views import *

admin.autodiscover()


urlpatterns = patterns('',
  
     #prologger vieews
     url(r'^$', index , name='index'),
     url(r'^login/', login_, name='login'),
     url(r'^logout/$', logout_, name='logout'),
     url(r'^api/account/achievements/',json_achievements),
     url(r'^achievements/$', achievements, name='achievements'),
     url(r'^analyze/$',analyze_achievements, name='analyze'),
     url(r'^profile/$', profile , name='profile'),
     url(r'^groups/$', groups , name='groups'),
     url(r'^home/$', home , name='home'),
     url(r'^about/$', home , name='about'),
     (r'^oauth/callback/', callback),

     #(r'^accounts/', include('registration.backends.default.urls')),
     # Uncomment the next line to enable the admin:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     (r'^admin/', include(admin.site.urls)),
     
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
