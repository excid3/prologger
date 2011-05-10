from django.db import models
from django.contrib.auth.models import User
from datetime import datetime




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
	
class ProloggerUser(models.Model):
	user = models.ForeignKey(User, unique=True)
	oauthtoken = models.CharField(max_length = 50)
	achievements = models.ManyToManyField(Achievement, blank=True)
	objects = ProloggerUserManager()
	
	def __unicode__(self):
		return u"Prologger information for %s" % self.user

	class Meta:
	    verbose_name_plural = "ProloggerUsers"

	def add_achievement(self, name):
            achievement = Achievement.objects.get(name=name)
            self.achievements.add(achievement)
            self.save()
