from django.shortcuts import render

# Create your views here.


def project_manage(request):
    return render(request, "spiderkeeper/project_manage.html")


def job_dashboard(request, project_id):
    job_status=JobExecution.list_jobs(project_id)
    context = {'job_status': job_status}
    return render(request, "spiderkeeper/job_dashboard.html", context)