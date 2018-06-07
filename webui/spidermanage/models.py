from django.db import models

class Project(models.Model):
    '''
    工程类型
    '''
    name = models.CharField(max_length=20, null=False, blank=False, db_index=True)
    version = models.CharField(max_length=20, null=False, blank=False)
    createtime = models.DateTimeField(auto_now_add=True)
    deployed = models.BooleanField(default=False)

    def __str__(self):
        return '{}({})'.format(self.name, self.version)

class Spider(models.Model):
    name = models.CharField(max_length=20)

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    spidername = models.CharField(max_length=20,null=False, blank=False)
    cron_expression = models.CharField(max_length=100)
    enable = models.BooleanField(default=True)
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True) 
    

    def __str__(self):
        return '{}-{} [{}]'.format(self.project, self.spidername, self.cron_expression)


class Job(models.Model):

    jobid = models.CharField(max_length=20)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    starttime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
    status = models.CharField(max_length=10)
    updatetime = models.DateTimeField(auto_now=True)