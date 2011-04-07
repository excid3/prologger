from django.conf.urls.defaults import *

# import in order to access settings.py variables
from django.conf import settings

# importing all the views  
from views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^prologger/', include('prologger.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^$', 'views.view', {'template': 'index.html'}, name='index'),
     (r'^login/', login),
     (r'^logout/', logout),
     ()
     (r'^analyze/',analyze_achievements),
     url(r'^about/$', 'views.view', {'template': 'about.html'}, name = 'about'),
     url(r'^home/$', 'views.view', {'template' : 'home.html'}, name = 'home'),
	 url(r'^profile/$', 'views.view', {'template' : 'profile.html'}, name = 'profile'),
	 url(r'^groups/$', 'views.view', {'template' : 'groups.html'}, name = 'groups'),
	 url(r'^faq/$', 'views.view', {'template' : 'faq.html'}, name = 'faq'),
     (r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^oauth/callback/', callback),
     (r'^oauth/token/', github_login),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
