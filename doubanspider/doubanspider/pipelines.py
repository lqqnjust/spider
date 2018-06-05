# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from .items import ImageItem
from scrapy.http import Request
import logging

logger = logging.getLogger()


class DownloadImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item,ImageItem):
            imgurl=item['image_url']
            yield Request(imgurl)

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        logger.info("iamgeguid:"+image_guid)
        return image_guid

class DjangoPipeline(object):
    def process_item(self, item, spider):
        try:
            item.save()
        except:
            pass
        return item
