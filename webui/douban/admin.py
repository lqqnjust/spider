from django.contrib import admin

from .models import Group
from .models import Topic
from .models import Image

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['groupname','grouplink','enable','max_page']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['topicid','title_link','author_link','visible']
    list_editable = ['visible']
    list_display_links = None
    list_filter = ['visible']
    ordering = ('-id',)
    list_per_page = 20

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['topicid','image','topic','author','visible']
    list_editable = ['visible']
    list_filter = ['visible']
    ordering = ('-id',)
    list_per_page = 10
