from django.contrib import admin

from .models import Project, Task , Job
from django.utils.html import format_html


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'version','operation',)

    def operation(self, obj):
        return format_html('<a href="#">部署</a> <a href="#">删除</a>')
    operation.short_description = 'operation'
