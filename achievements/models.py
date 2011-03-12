from django.db import models

class Achievements(models.Model):
	name = models.CharField(max_length = 40)
	points = models.IntegerField()
	date = model.DateField(auto_now_add=True)
	description = models.CharField(max_length = 140)
	
	def __unicode__(self):
        return self.name
	
class ProloggerUser(model.Model):
	user = models.ForeignKey(User, unique=True)
	achievements = models.ForeignKey(Achievements)
