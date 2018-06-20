from django.db import models

# Create your models here.
from .scrapydapi import listspiders, addversion
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    eggfile = models.FileField(upload_to='eggs')
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.version)


    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        print(self.eggfile)
        addversion(self.name,self.version, settings.MEDIA_ROOT + "/"+self.eggfile.name)

        spiders = listspiders(self.name)
        spidermodels = Spider.objects.all().filter(project=self)
        spidernamesinmodel = [ x.name for x in spidermodels]
        need = []
        for spider in spiders:
            if spider not in spidernamesinmodel:
                need.append(spider)
        for spider in need:
            sp = Spider()
            sp.name = spider
            sp.project = self
            sp.save()



class Spider(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Task(models.Model):
    SCHEDULER_TYPE = (
        (0,'interval'),
        (1,'crontab')
    )
    name = models.CharField(max_length=100)
    spider = models.ForeignKey(Spider, on_delete=models.CASCADE)
    remark = models.TextField(null=True,blank=True)
    argument = models.TextField(null=True,blank=True)
    expression = models.TextField(max_length=200,blank=True)
    type = models.IntegerField(choices=SCHEDULER_TYPE)
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    jobid = models.CharField(max_length=100)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    starttime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
    creattime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.jobid
