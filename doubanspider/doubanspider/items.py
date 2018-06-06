# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy




class TopicItem(DjangoItem):
	django_model = Topic


class ImageItem(DjangoItem):
	django_model = Image
