# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#明确需要提取的数据
class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    JobTitle  = scrapy.Field()
    JobLink = scrapy.Field()
    JobType = scrapy.Field()
    Numbers = scrapy.Field()
    WorkPlace = scrapy.Field()
    ReleaseTime = scrapy.Field()