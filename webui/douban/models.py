from django.db import models
from django.utils.html import format_html

class Group(models.Model):
    groupname = models.CharField(verbose_name=u'小组名', max_length=200)
    grouplink = models.CharField(verbose_name=u'小组链接',max_length=200)
    enable = models.BooleanField(verbose_name=u'是否生效',default=False)
    max_page = models.IntegerField(verbose_name=u'获取最大页数',default=1)


class Topic(models.Model):
    topicid = models.IntegerField(verbose_name=u'ID',unique=True)
    title = models.CharField(verbose_name=u'标题',max_length=200)
    title_url = models.CharField(verbose_name=u'标题链接',max_length=200,default='')
    content = models.TextField(verbose_name=u'内容',default='')
    author_name = models.CharField(verbose_name=u'作者',max_length=50)
    author_url = models.CharField(verbose_name=u'主页',max_length=200)
    groupid = models.IntegerField(verbose_name=u'分组id',default=0)
    visible = models.BooleanField(verbose_name=u'是否显示',default=True)

    def title_link(self):
        return format_html(
            '<a href="{}">{}</a>',
            self.title_url,
            self.title,
        )

    def author_link(self):
        return format_html(
            '<a href="{}">{}</a>',
            self.author_url,
            self.author_name,
        )


class Image(models.Model):
    topicid = models.IntegerField(verbose_name=u'主题ID')
    image_url = models.CharField(verbose_name=u'图片地址',max_length=200,unique=True)
    visible = models.BooleanField(verbose_name=u'是否显示',default=True)

    def image(self):
        return format_html(
            '<img width=100 height=100 src="/media/doubanspider/{}"/>',
            self.image_url.split("/")[-1]
        )

    def topic(self):
        topic= Topic.objects.get(topicid=self.topicid)
        return format_html(
            '<a href="{}">{}</a>',
            topic.title_url,
            topic.title,
        )

    def author(self):
        topic = Topic.objects.get(topicid=self.topicid)
        return format_html(
            '<a href="{}">{}</a>',
            topic.author_url,
            topic.author_name,
        )