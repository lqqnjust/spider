from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import ProjectView

urlpatterns = [
    path('', views.index, name='index'),
    path('/projects', ProjectView.as_view(), name='projects')
]