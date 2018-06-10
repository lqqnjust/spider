from django.contrib import admin

from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','version','createtime')

@admin.register(Spider)
class SpiderAdmin(admin.ModelAdmin):
    list_display = ('name','project')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','spider','remark','argument','expression','type','createtime','updatetime')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('jobid','task','starttime','endtime','creattime','updatetime','status')