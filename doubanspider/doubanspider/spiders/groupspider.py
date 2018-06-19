# coding:utf-8

import scrapy
from doubanspider.items import TopicItem, ImageItem

import re
from scrapy.http import Request
from scrapy.utils.project import get_project_settings

import logging
import sqlite3

class GroupSpider(scrapy.Spider):
    name = "doubangroup"


    def start_requests(self):
        # groups = Group.objects.filter(enable=True)
        # for group in groups:
        #     yield self.make_requests_from_url(group.grouplink)
        settings = get_project_settings()
        sqlite_file = settings.get('SQLITE_FILE')
        conn = sqlite3.connect(sqlite_file)
        cur = conn.cursor()
        sql = "select grouplink, max_page from douban_group where enable=1"
        cur.execute(sql)
        records = cur.fetchall()
        for record in records:
            grouplink = record[0]
            max_page  = record[1]
            for x in range(max_page):
                url = "%s/discussion?start=%d" %(grouplink, x*25)
                logging.info("url")
                yield self.make_requests_from_url(url)
        cur.close()

    def parse(self, response):
        for sel in response.xpath('//tr[@class=""]'):
            item = TopicItem()
            item['title'] = sel.xpath('td[1]/a//text()').extract()[0]
            item['title_url'] = sel.xpath('td[1]/a//@href').extract()[0]
            item['topicid'] = re.search(r'\d+', item['title_url']).group()
            item['author_name'] = sel.xpath('td[2]/a//text()').extract()[0]
            item['author_url'] = sel.xpath('td[2]/a//@href').extract()[0]
            item['content'] = ''
            item['groupid'] = 0

            # entrys = Topic.objects.filter(topicid=int(item['topicid']))

            # if len(entrys)==0:
            # if True:
            yield item
            self.logger.info(item)
            yield Request(item['title_url'], callback=self.parse_item, meta={'topicid': item['topicid']})

    # 2. parse image urls
    def parse_item(self, response):
        topicid = response.meta['topicid']
        image_urls = response.xpath('//div[@class="image-wrapper"]/img/@src').extract()
        for url in image_urls:
            item = ImageItem()
            item['topicid'] = topicid
            if url.endswith(".webp"):
                url = url.replace("webp","jpg")
            item['image_url'] = url
            yield item
            self.logger.info(item)
