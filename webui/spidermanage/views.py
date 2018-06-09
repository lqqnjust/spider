import tempfile

from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView

from .models import Project, Task

from .scrapydapi import *

def index(request):
    projects = Project.objects.all()
    context = {}
    context['projects'] = projects
    return render(request, 'spidermanage/index.html',context)


class ProjectView(ListView):
    queryset = Project.objects.all()
    context_object_name = 'projects'
    template_name = 'spidermanage/projects.html'

def project(request, pk):
    projects = Project.objects.all()
    print(projects)
    context = {}
    context['projects'] = projects
    project = Project.objects.get(id=pk)
    context['project'] = project
    
    context['tasks'] =  Task.objects.all().filter(project=project.name)

    spiders = listspiders(project.name)
    print(spiders)
    context['spiders'] = spiders

    jobs = Job.objects.all().filter(projectname=project.name)
  

    return render(request, 'spidermanage/project.html',context)


def addNewProject(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        context = {}
        context['projects'] = projects

        return render(request, 'spidermanage/newproject.html', context )
    else:
        filedata = request.FILES['file']
        projectname = request.POST['projectname']
        project, created = Project.objects.get_or_create(name=projectname)
        with open('douban.egg','wb') as f:
            for chunk in filedata.chunks():
                f.write(chunk)
        
        addversion(projectname, "douban.egg")
        return redirect("/spider/project/{}".format(project.id))


def addTask(request):
    projectid = request.POST['projectid']
    projectname = request.POST['project']
    spidername = request.POST['spidername']
    argument = request.POST['argument']
    cron_expression = request.POST['cron_expression']

    task = Task()
    task.project = projectname
    task.spidername = spidername
    task.argument = argument
    task.cron_expression = cron_expression
    task.save()

    return redirect('/spider/project/{}'.format(projectid))

def delTask(request, pk):
    task = Task.objects.get(id=pk)
    projectname = task.project
    task.delete()

    project = Project.objects.get(name=projectname)

    return redirect('/spider/project/{}'.format(project.id)) 

