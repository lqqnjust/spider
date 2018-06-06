# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TopicItem(scrapy.Item):
	topicid = scrapy.Field()
	title = scrapy.Field()
	title_url = scrapy.Field()
	content = scrapy.Field()
	author_name = scrapy.Field()
	author_url = scrapy.Field()
	groupid = scrapy.Field()
	


class ImageItem(scrapy.Item):
    topicid = scrapy.Field()
    image_url = scrapy.Field()
    
