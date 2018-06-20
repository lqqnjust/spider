from .models import Project, Job,Spider
from .scrapydapi import listjobs, listspiders,listprojects,addversion

from django.conf import settings
import logging
import datetime
from django.utils import timezone

def sync_job_execution_status_job():
    '''
    sync job execution running status
    :return:
    '''
    projects = Project.objects.all()
    for project in projects:
        data = listjobs(project.name)
        if data is not None:
            pending,running,finished = data
            for job in pending:
                id = job['id']
                try:
                    job = Job.objects.get(jobid=id)
                    job.status = "pending"
                    job.save()
                except:
                    logging.error("job not exists, jobid:"+id)
            for job in running:
                id = job['id']
                start_time = job['start_time']
                try:
                    job = Job.objects.get(jobid=id)
                    job.status = "running"
                    start_datetime = timezone.datetime.strptime(start_time[:18],'%Y-%m-%d %H:%M:%S')
                    job.starttime = start_datetime
                    job.save()
                except:
                    logging.error("job not exists, jobid:"+id)
            for job in finished:
                id = job['id']
                start_time = job['start_time']
                end_time = job['end_time']
                try:
                    job = Job.objects.get(jobid=id)
                    job.status = "finished"
                    start_datetime = timezone.datetime.strptime(start_time[:18],'%Y-%m-%d %H:%M:%S')
                    end_datetime = timezone.datetime.strptime(end_time[:18],'%Y-%m-%d %H:%M:%S')
                    job.starttime = start_datetime
                    job.endtime = end_time
                    job.save()
                except:
                    logging.error("job not exists, jobid:"+id)
                

def check_project():
    projects = listprojects()
    if len(projects) == 0:
        project_models = Project.objects().all()
        if len(project_models) > 0:
            for project_model in project_models:
                addversion(project_model.name,project_model.version, settings.MEDIA_ROOT + "/"+project_model.eggfile.name)

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

from .schedulers import sync_job_execution_status_job,sync_spiders,reload_runnable_spider_job_execution

scheduler.add_job(sync_job_execution_status_job, 'interval', seconds=10, id='sys_sync_status')
scheduler.add_job(check_project, 'interval', seconds=60, id='check_project')

def init():
    scheduler.start()