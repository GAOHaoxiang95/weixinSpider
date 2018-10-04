# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlencode
from weixin.items import WeixinItem
from urllib.parse import urlunsplit, urlsplit

	
	
	
class ArticleSpider(CrawlSpider):
    name = 'article'
    url = "https://weixin.sogou.com/weixin?"
    keyword = 'NBA'
	
	
    param = urlencode({'type': 2, 'query':keyword})
	

    allowed_domains = ['weixin.sogou.com', 'mp.weixin.qq.com']
    start_urls = [url + param]

	#id = sogou_next
    rules = (
        Rule(LinkExtractor(allow='http:\/\/mp\.weixin\.qq.com\/s.*', restrict_xpaths='//*[@class="news-box"]'), callback = 'parse_item'),
		Rule(LinkExtractor(restrict_xpaths='//*[@id="sogou_next"]'))
    )

    def parse_item(self, response):
        item = WeixinItem()
        item['time'] = re.search('\d\d\d\d-\d\d-\d\d', response.text).group()#javascript
        item['nickname'] = response.xpath('//*[@id="js_name"]/text()').extract_first()
        item['title'] = response.xpath('//title/text()').extract_first()
        
        return item
		

		
		