from django.contrib import admin
from achievements.models import Achievements, ProloggerUser


class AchievementsAdmin(admin.ModelAdmin):
	pass

class ProloggerUserAdmin(admin.ModelAdmin):
	list_display = ('user', 'achievements')
	
admin.site.register(Achievements, AchievementsAdmin)
admin.site.register(ProloggerUser, ProloggerUserAdmin)
