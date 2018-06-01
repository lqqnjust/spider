from django.db import models

# Create your models here.


class Project(models.Model):

    project_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table="sk_project" 


class SpiderInstance(models.Model):
    spider_name = models.CharField(max_length=100)
    project_id = models.IntegerField(unique=True, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table="sk_spider"  

JobRunType = {
    (0, 'ontime'),
    (1, 'periodic')
}
JobPriority = {
    (-1, 'LOW'),
    (0, 'NORMAL'),
    (1, 'HIGH'),
    (2, 'HIGHEST')
}

class JobInstance(models.Model):

    spider_name = models.CharField(max_length=100)
    project_id = models.IntegerField(null=False, db_index=True)
    tags = models.TextField()
    spider_arguments = models.TextField()
    priority = models.IntegerField(choices=JobPriority)
    desc = models.TextField()
    cron_express = models.CharField(max_length=500)
    enabled = models.BooleanField(default=True)
    run_type = models.IntegerField(choices=JobRunType)

    class Meta:  
        db_table="sk_job_instance"

SpiderStatus = {
    (0, 'PENDING'),
    (1, 'RUNNING'),
    (2, 'FINISHED'),
    (3, 'CANCELED')
}