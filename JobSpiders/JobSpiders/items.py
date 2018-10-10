# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class JobspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Job51ItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class Job51Item(ItemLoader):
    url = scrapy.Field()
    url_obj_id = scrapy.Field()
    title = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    job_city = scrapy.Field()
    experience_year = scrapy.Field()
    education_need = scrapy.Field()
    publish_date = scrapy.Field()
    job_advantage_tags = scrapy.Field()
    position_info = scrapy.Field()
    job_classification = scrapy.Field()
    crawl_time = scrapy.Field()

def remove_splash(value):
    #去掉工作城市的斜线
    return value.replace("/", "")

def handle_jobaddr(value):
    addr_list = value.split("\n")
    addr_list = [item.strip() for item in addr_list if item.strip()!="查看地图"]
    return "".join(addr_list)


