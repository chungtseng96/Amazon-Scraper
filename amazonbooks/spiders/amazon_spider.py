# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonbooksItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_num = 2
    start_urls = [
        'https://www.amazon.com/s?i=stripbooks&rh=n%3A283155%2Cn%3A1000%2Cn%3A3%2Cn%3A2581%2Cn%3A2588&qid=1564515430&ref=sr_pg_1'
    ]

    def parse(self, response):
        items = AmazonbooksItem()
        
        product_name = response.css('.a-size-medium.a-color-base.a-text-normal::text').extract()
        product_author = response.css('a-size-base a-link-normal').css('::text').extract()
        product_price = response.css('.a-spacing-none:nth-child(2) .sx-price-fractional , .a-spacing-none:nth-child(2) .sx-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        
        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink
       
        next_page = 'https://www.amazon.com/s?i=stripbooks&rh=n%3A283155%2Cn%3A1000%2Cn%3A3%2Cn%3A2581%2Cn%3A2588&page=2&qid=1564515502&ref=sr_pg_' + str(AmazonSpiderSpider.page_num)
        
        if AmazonSpiderSpider.page_num <= 10:
            AmazonSpiderSpider.page_num += 1 
            yield response.follow(next_page, callback = self.parse)
        
        
        
        
        
