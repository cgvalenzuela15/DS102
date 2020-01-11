# -*- coding: utf-8 -*-
import scrapy


class PaginationSpider(scrapy.Spider):
    name = 'Pagination'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for books in response.css('article.product_pod'):
            yield {
                'Title':books.css('h3>a::attr(href)').extract(),
                'Product Price':books.css('p.price_color::text').extract(),
                'Product Availability':books.css('p.instock.availability::text').extract()
            }
        next_page_url = response.css('li.next>a::attr(href)').extract_first()
        if next_page_url:
            next_page = response.urljoin(next_page_url)
        yield scrapy.Request(url = next_page, callback=self.parse)