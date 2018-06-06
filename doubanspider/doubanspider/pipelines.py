# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from .items import ImageItem, TopicItem
from scrapy.http import Request
import logging
import sqlite3



class DownloadImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item,ImageItem):
            imgurl=item['image_url']
            yield Request(imgurl)

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        logging.info("iamgeguid:"+image_guid)
        return image_guid

class DjangoPipeline(object):
    
    def __init__(self,sqlite_file):
        self.sqlite_file = sqlite_file
    def open_spider(self,spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_file = crawler.settings.get('SQLITE_FILE'), # 从 settings.py 提取
        )

    def process_item(self, item, spider):
        sql = None
        if isinstance(item, TopicItem):
            sql = "insert into douban_topic ({}) values ({})".format(', '.join(item.fields.keys()),
                                                                ', '.join(['?'] * len(item.fields.keys())))
            
        elif isinstance(item, ImageItem):
            sql = "insert into douban_image ({}) values ({})".format(', '.join(item.fields.keys()),
                                                                ', '.join(['?'] * len(item.fields.keys())))
        logging.info("sql:"+sql)
        logging.info("items:"+str(item))
        logging.info("keys:"+str(item.fields.keys()))
        self.cur.execute(sql,[item[x] for x in item.fields.keys()])
        self.conn.commit()
   

        return item

