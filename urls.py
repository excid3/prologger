from django.conf.urls.defaults import *

# import in order to access settings.py variables
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# importing all the views  
from views import *

admin.autodiscover()

#JavaScript functionality
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^prologger/', include('prologger.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# Added for JavaScript functionality
	 (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
     url(r'^$', 'views.view', {'template': 'index.html'}, name='index'),
     url(r'^login/', login_, name = 'login'),
     url(r'^logout/$', logout_, name = 'logout'),
     url(r'^analyze/$',analyze_achievements, name = 'analyze'),
     url(r'^about/$', 'views.view', {'template': 'about.html'}, name = 'about'),
     url(r'^home/$', 'views.view', {'template' : 'home.html'}, name = 'home'),
	 url(r'^profile/$', 'views.view', {'template' : 'profile.html'}, name = 'profile'),
	 url(r'^groups/$', 'views.view', {'template' : 'groups.html'}, name = 'groups'),
	 url(r'^faq/$', 'views.view', {'template' : 'faq.html'}, name = 'faq'),
	 url(r'^privacyPolicy/$', 'views.view', {'template' : 'privacyPolicy.html'}, name = 'privacyPolicy'),
	 url(r'^contact/$', 'views.view', {'template' : 'contact.html'}, name = 'contact'),
     #(r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^oauth/callback/', callback),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
