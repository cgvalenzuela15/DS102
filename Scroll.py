# -*- coding: utf-8 -*-
import scrapy
import json

class ScrollSpider(scrapy.Spider):
    name = 'Scroll'
    allowed_domains1 = 'http://jsonplaceholder.typicode.com/posts?_page=$s'
    start_urls = ['http://jsonplaceholder.typicode.com/posts']
    download_delay = 1.5

    def parse(self, response):
        json_data = json.loads(response.text)
        for item in json_data:
                yield item
        if json_data:
                yield scrapy.Request(self.allowed_domains1 % (int(json_data['page']) + 1))