from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
# Python
import oauth2 as oauth
import cgi


# import in order to access settings.py variables
from settings import MEDIA_URL
#allow for redirections after work to reload a page with new data
from django.http import HttpResponseRedirect
#github api
from github2.client import Github

from achievements.models import ProloggerUser

from achievements_analytics import AchievementsAnalytics

from django.template import RequestContext

def view(request, template):
	c = {}
	media = {'MEDIA_URL' : MEDIA_URL }
	c.update(csrf(request))
	c.update(media)
	username = request.POST.get('username', '')
	api_token = request.POST.get('api_token', '')
	github = Github(username=username, api_token=api_token)
	gh = {'github': github}
	#creating a dictionary for context
	u = {'username': username}
	# adding d to c dictionary
	c.update(u)
	c.update(gh)
	return render_to_response(template,  c)
	
def analyze_achievements(request):
	user = request.user
	prologger_user = ProloggerUser.objects.get(user=user)
	github_user = prologger_user.github_user
	github_apitoken = prologger_user.github_apitoken 
	ach = AchievementsAnalytics(github_user, github_apitoken, prologger_user)
	achi = ach.get_achievements()
	html = "<html><body>The current user is  %s, prologger_user is : %s, the github user : %s, and the api_token %s.</body><p>%s</p></html>" % (user, prologger_user , github_user, github_apitoken, achi)
	return HttpResponse(html)
	

def github_login(request):
	pass
def callback(request):
	
	code =request.code
	if code = None:
		code = woohoo
	html= "<html><body>%s</body></html>" % (code)
	return HttpResponse(html)
	

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
	
