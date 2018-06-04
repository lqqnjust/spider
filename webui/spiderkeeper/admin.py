from django.contrib import admin

from .models import *


@admin.register(Project)
class PrjectAdmin(admin.ModelAdmin):
	pass


@admin.register(SpiderInstance)
class SpiderInstanceAdmin(admin.ModelAdmin):
	pass


@admin.register(JobInstance)
class JobInstanceAdmin(admin.ModelAdmin):
	pass


@admin.register(JobExecution)
class JobExecutionAdmin(admin.ModelAdmin):
	pass