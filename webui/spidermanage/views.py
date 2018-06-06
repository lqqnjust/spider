from django.shortcuts import render
from django.views.generic import ListView

from .models import Project

def index(request):
    return render(request, 'spidermanage/index.html')


class ProjectView(ListView):
    queryset = Project.objects.all()
    context_object_name = 'projects'
    template_name = 'spidermanage/projects.html'