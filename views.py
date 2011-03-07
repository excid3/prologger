from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf

# import in order to access settings.py variables
from settings import MEDIA_URL
#allow for redirections after work to reload a page with new data
from django.http import HttpResponseRedirect
#github api
from github2.client import Github

from django.template import RequestContext

def view(request, template):
	c = {}
	c.update(csrf(request))
	try:
		username = request.POST.get('username', '')
		password = request.POST.get('api_token', '')
		#creating a dictionary for context
		d = {'username': username, "MEDIA_URL": MEDIA_URL}
		# adding d to c dictionary
		c.update(d)
		print c
	except:
		print c
		user = ''
	return render_to_response(template,  c)
	
def login(request):
	username = request.POST.get('username', '')
	api_token = request.POST.get('api_token', '')
	github = Github(username=username, api_token=api_token)
	print github
	if github is not None:
		return HttpResponseRedirect("/")
	else:
		# Show an error page
		return HttpResponseRedirect("/")
		
def loggedin(request):
	pass
	
