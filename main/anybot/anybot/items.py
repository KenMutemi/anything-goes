# -*- coding: utf-8 -*-
from scrapy.item import Item, Field
import scrapy

class AnyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
