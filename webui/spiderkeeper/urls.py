# coding:utf-8

from django.contrib import admin
from django.urls import path, include

from .views import project_manage
from .views import project_create
from .views import spider_deploy
from .views import project_index
from .views import job_dashboard

urlpatterns = [
    path('manage/', project_manage),
    #path('<project_id>/job/dashboard')
    path('create/', project_create),
    path('<project_id>/spider/deploy/', spider_deploy),
    path('<project_id>/', project_index),
    path('<project_id>/job/dashboard/', job_dashboard)
]