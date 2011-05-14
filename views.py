#Django
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import simplejson
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required


# Python
import oauth2 as oauth
import cgi
import urlparse
import urllib
#Prologger
from github2.client import Github
from achievements.models import ProloggerUser, Achievement
from achievements_analytics import AchievementsAnalytics
from settings import MEDIA_URL, DEBUG

# Github OAuth urls
authorize_url = 'https://github.com/login/oauth/authorize?'
access_token_url = 'https://github.com/login/oauth/access_token?'
if DEBUG:
    redirect_url = 'http://127.0.0.1:8000/oauth/callback/'
    # consumer secret and key needed to authenticate prologger as a valid Github OAuth application
    #TODO move these to settings.py
    consumer_key ='23f031a141390affb072'
    consumer_secret = '27844d1838266470b876e29fbbbb2b303c8ea7f1'
else:
    redirect_url = 'http://prologger.ep.io/oauth/callback/'
    # consumer secret and key needed to authenticate prologger as a valid Github OAuth application
    #TODO move these to settings.py
    consumer_key ='c4e2f51b2faaed2d1762'
    consumer_secret = 'ca01dbc8e37a89b6de54e48fec27d85e02289314'

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)


def index(request):
    """ 
    landing page view user login and greeting

    """
    return render(request,'index.html')

def profile(request):
    """
    user profile view
    
    here we will put shit like user profile recently asked questions and github achievements
    
    """
    return render(request,'profile.html')

def home (request):
    """ 

    I am hoping to have a news feed type of things for user to see what their friends are up to.

    """
    return render(request,'home.html')


def groups(request):
    """

    Groups page shows what the dev teams you are part of recent team member stats and achievements

    """
    return render(request,'groups.html')

def achievements(request):
    """
    This page is mostly here for testing may not exist in the future. ajax page for the achievements
    """
    user = request.user
    prologger_user = ProloggerUser.objects.get(user=user)
    achievements =  prologger_user.achievements.all()
    print achievements
    data = {}
    data.update({'user': prologger_user.user})
    data.update({'achievements': achievements})
    return render(request,'achievements.html', data)

@login_required(login_url='/')
def analyze_achievements(request):
    """
    This is the current analyze page for the user it allows user to ping to cause an analysis of thier current achievement and renders a simple page fast. 
    """
    user = request.user
    prologger_user = ProloggerUser.objects.get(user=user)
    oauthtoken = prologger_user.oauthtoken
    ach = AchievementsAnalytics(oauthtoken, prologger_user)
    achi = ach.get_achievements()
    html = "<html><body>The current user is  %s, prologger_user is : %s.</body><p>%s</p></html>" % (user, prologger_user , achi)
    return HttpResponse(html)

def json_achievements(request):

    """
    This is the first of many prologger end points for ajax to hit against for pseudo realtime user experience 
    """
    user = request.user
    if isinstance(user, AnonymousUser):
       error =  {'error': "You need to be logged in"}
       json = simplejson.dumps(error)
       return HttpResponse(json, mimetype='application/json')
    prologger_user = ProloggerUser.objects.get(user=user)
    oauthtoken = prologger_user.oauthtoken
    achievements = AchievementsAnalytics(oauthtoken, prologger_user)
    json_achievements = achievements.get_achievements()
    json = simplejson.dumps(json_achievements)
    return HttpResponse(json, mimetype='application/json')

def create_prologgeruser(name, email, token):
    """
    method to create a prologger user and user give 
    """
    if email is None:
        user = User.objects.create_user(username=name, password = token )
    else:
        user = User.objects.create_user(username=name, email=email, password = token )
    # Save our permanent token and secret for later.
    profile = ProloggerUser()
    profile.user = user
    profile.oauthtoken = token
    profile.save()
	
def callback(request):
    """
    This is the function dealing with the github authentication. needs to be refactored and cleaned. 

    """
    # @see https://gist.github.com/960593

    code = request.GET['code']
    url = "%sclient_id=%s&redirect_uri=%s&client_secret=%s&code=%s" % (access_token_url, consumer_key, redirect_url, consumer_secret, code)
    print url
    f =  urllib.urlopen(url)
    response = dict(cgi.parse_qsl(f.read()))
    print response
    token =  response['access_token']
    github = Github(access_token=token)
    #kludge to get current user
    name =  github.users.show("")
    print name.login
    print name.email
    
    try:
        user = User.objects.get(username=name.login)
    except User.DoesNotExist:
        create_prologgeruser(name.login,name.email,token)
        
    # Authenticate the user and log them in using Django's pre-built 
    # functions for these things.
    print str(name.login)
    print token
    user = authenticate(username=str(name.login),password=str(token))
    print user
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/analyze/')
    else:
        return HttpResponseRedirect('/')
    
def logout_(request):
    """
    Standard logout view
    """
    logout(request)
    return HttpResponseRedirect('/')
     

def login_(request):
    """
    This is the login in view which ends up going to the callback view for the Github OAuth
    """
    resp, content = client.request(authorize_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response %s." % resp['status'])
    request_token = dict(urlparse.parse_qsl(content))
    url = "%sclient_id=%s&redirect_uri=%s" % (authorize_url, consumer_key, redirect_url)
    return HttpResponseRedirect(url)
	
