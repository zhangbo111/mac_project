# -*- coding: utf-8 -*-
import scrapy


class MyjySpider(scrapy.Spider):
    name = 'myjy'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
