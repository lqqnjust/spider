from django.shortcuts import render
from django.shortcuts import redirect

from .models import Project
from .models import JobExecution


def project_manage(request):

    projects = Project.objects.all()
    
    context = {}
    context['project_list'] = projects
    if len(projects) > 0:
        context['project'] = projects[0]


    return render(request, "spiderkeeper/project_manage.html", context)


# def job_dashboard(request, project_id):
#     job_status=JobExecution.list_jobs(project_id)
#     context = {'job_status': job_status}
#     return render(request, "spiderkeeper/job_dashboard.html", context)



def project_create(request):
    '''
    创建工程
    '''
    if request.method == "POST":
        project_name = request.POST['project_name']
        print(project_name)
        project = Project()
        project.project_name = project_name
        project.save()

        return redirect("/{}/spider/deploy/".format(project.id), project = project)



def spider_deploy(request,project_id):
    '''
    部署爬虫
    '''
    project = Project.objects.get(id=project_id)
    return render(request, "spiderkeeper/spider_deploy.html",context={"project":project})


def project_index(request, project_id):
    '''
    project首页
    '''
    request.session['project_id'] = project_id
    return redirect("/{}/job/dashboard".format(project_id))

def job_dashboard(request, project_id):
    '''
    显示工程下所有任务状态
    '''
    job_status=job_status=JobExecution.list_jobs(project_id)
    context = {}
    context['job_status'] = job_status
    return render(request, "spiderkeeper/job_dashboard.html",context=context)