from django.contrib import admin

from .models import *
from .scrapydapi import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','version','createtime')

@admin.register(Spider)
class SpiderAdmin(admin.ModelAdmin):
    list_display = ('name','project')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','spider','remark','argument','expression','type','createtime','updatetime')
    actions  = ['run_once']

    def run_once(self, request, queryset):
        for task in queryset:
            jobid = schedule(task.spider.project.name,task.spider.name, {})
            job = Job()
            job.jobid = jobid
            job.task = task
            job.save()
        self.message_user(request, "%d 个任务已启动" % len(queryset))
    run_once.short_description = "立即执行"

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('jobid','task','starttime','endtime','creattime','updatetime','status')