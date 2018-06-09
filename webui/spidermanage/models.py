from django.db import models

class Project(models.Model):
    '''
    工程类型
    '''
    name = models.CharField(max_length=20, null=False, blank=False, db_index=True)
    
    createtime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.CharField(max_length=20)
    spidername = models.CharField(max_length=20,null=False, blank=False)
    cron_expression = models.CharField(max_length=100)
    createtime = models.DateTimeField(auto_now_add=True)
    argument=models.TextField(default='',blank=True)
    updatetime = models.DateTimeField(auto_now=True) 
    enable = models.BooleanField(default=True)
    

    def __str__(self):
        return '{}-{} [{}]'.format(self.project, self.spidername, self.cron_expression)


class Job(models.Model):

    jobid = models.CharField(max_length=20)
    taskname = models.CharField(max_length=20)
    projectname = models.CharField(max_length=20)
    starttime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
    status = models.CharField(max_length=10)
    updatetime = models.DateTimeField(auto_now=True)