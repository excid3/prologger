from django.db import models
from django.contrib.auth.models import User




class ProloggerUserManager(models.Manager):
	def create_user(self, user):
		pro = ProloggerUser(user = user)
		pro.save()
		
class AchievementsManager(models.Manager):
	pass
	
		
class Achievements(models.Model):
	name = models.CharField(max_length = 40)
	points = models.IntegerField(blank=True, null = True)
	date = models.DateField(auto_now_add=True)
	description = models.CharField(max_length = 140)
	objects = AchievementsManager()	
	def __unicode__(self):
		return self.name
	
class ProloggerUser(models.Model):
	user = models.ForeignKey(User, unique=True)
	achievements = models.ManyToManyField(Achievements, blank=True)
	github_user = models.CharField(max_length=23)
	github_apitoken = models.CharField(max_length=40)
	objects = ProloggerUserManager()
	
	def __unicode__(self):
		return u"Prologger information for %s" % self.user
