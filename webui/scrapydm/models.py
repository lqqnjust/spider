from django.db import models

# Create your models here.


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
    remark = models.TextField()
    argument = models.TextField()
    expression = models.TextField(max_length=200)
    type = models.IntegerField(choices=SCHEDULER_TYPE)
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)

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
