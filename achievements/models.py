from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ModelForm





class ProloggerUserManager(models.Manager):
	def create_user(self, user):
		pro = ProloggerUser(user = user)
		pro.save()
		
class AchievementsManager(models.Manager):
	def create_achievement(self, name, description, points = None):
		achievement = Achievement(name=name, description=description, points=points)
		achievement.save()
       
class Achievement(models.Model):
	name = models.CharField(max_length = 40)
	points = models.IntegerField(blank=True, null = True)
	description = models.CharField(max_length = 140)
	def __unicode__(self):
		return self.name
		
	class Meta:
	    verbose_name_plural = "Achievements"

# @see for more information on available fields  http://docs.djangoproject.com/en/dev/ref/models/fields/

class ProloggerUser(models.Model):
	user = models.ForeignKey(User, unique=True)
	oauthtoken = models.CharField(max_length=50)
	achievements = models.ManyToManyField(Achievement, blank=True)
	email = models.EmailField(max_length=75, blank=True)
	name = models.CharField(max_length=50, blank= True)
	website = models.CharField(max_length=75, blank= True)
	profile_pic = models.ImageField(upload_to='profile_pictures', default='/home/myusuf3/Github/prologger/static/defaultPortrait.png')
	objects = ProloggerUserManager()
	
	def __unicode__(self):
		return u"Prologger information for %s" % self.user

	class Meta:
	    verbose_name_plural = "ProloggerUsers"

	def add_achievement(self, name):
            achievement = Achievement.objects.get(name=name)
            self.achievements.add(achievement)
            self.save()

class ProloggerUserForm(ModelForm):
	class Meta:
		model = ProloggerUser
		exclude = ('oauthtoken','achievements','user')