from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project, Task

from .scrapydapi import *

def index(request):
    return render(request, 'spidermanage/index.html')


class ProjectView(ListView):
    queryset = Project.objects.all()
    context_object_name = 'projects'
    template_name = 'spidermanage/projects.html'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'spidermanage/project.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        
        tasks = Task.objects.filter(project__id=self.object.id)
        context['tasks'] = tasks

        spiders = listspiders(self.object.name)
        context['spiders'] = spiders
        return context

