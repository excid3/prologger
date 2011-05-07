from django.db import models
from django.contrib.auth.models import User
from datetime import datetime




class ProloggerUserManager(models.Manager):
	def create_user(self, user):
		pro = ProloggerUser(user = user)
		pro.save()
		
class AchievementsManager(models.Manager):
	def create_achievement(self, name, date, description, points = None):
		achievement = Achievements(name = name, date = date, description = description, points = points)
		achievement.save()
        
	
		
class Achievements(models.Model):
	name = models.CharField(max_length = 40)
	points = models.IntegerField(blank=True, null = True)
	date = models.DateField(auto_now_add=True)
	description = models.CharField(max_length = 140)
	def __unicode__(self):
		return self.name
		
	class Meta:
	    verbose_name_plural = "Achievements"
	
class ProloggerUser(models.Model):
	user = models.ForeignKey(User, unique=True)
	oauthtoken = models.CharField(max_length = 50)
	achievements = models.ManyToManyField(Achievements, blank=True)
	objects = ProloggerUserManager()
	
	def __unicode__(self):
		return u"Prologger information for %s" % self.user
	class Meta:
	    verbose_name_plural = "ProloggerUsers"
