from django.contrib import admin
from achievements.models import Achievement, ProloggerUser


class AchievementsAdmin(admin.ModelAdmin):
	pass

class ProloggerUserAdmin(admin.ModelAdmin):
    pass
	
admin.site.register(Achievement, AchievementsAdmin)
admin.site.register(ProloggerUser, ProloggerUserAdmin)
