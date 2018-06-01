# coding:utf-8

from django.contrib import admin
from django.urls import path, include

from .views import project_manage

urlpatterns = [
    path('manage/', project_manage),
    #path('<project_id>/job/dashboard')
]