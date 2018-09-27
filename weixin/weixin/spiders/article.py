# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArticleSpider(CrawlSpider):
    name = 'article'
	url = "http://weixin.sogou.com/weixin?type=2&query=%E6%80%AA%E7%89%A9%E7%8C%8E%E4%BA%BA"
    allowed_domains = ['weixin.sogou.com']
    start_urls = ['http://weixin.sogou.com/']

	
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
