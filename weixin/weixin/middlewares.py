# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals
import json
import logging
import requests
agents = [
'http://123.161.238.209:32724',
'http://14.115.69.8:48768',
'http://123.101.141.235:27959',
'http://113.103.116.48:33440',
'http://171.12.166.96:46924',
'http://113.117.64.65:36811',
'http://114.230.97.139:29392',
'http://113.110.47.253:33361',
'http://183.142.119.187:46752',
'http://171.12.167.144:44596',
'http://123.54.226.87:25866',
'http://182.202.223.17:40457',
'http://182.202.222.181:39924',
'http://117.94.181.156:24628',
'http://111.72.193.196:44953',
'http://49.67.167.247:41055',
'http://14.118.235.76:21531',
'http://183.154.50.114:27277',
'http://36.25.40.47:46852',
'http://125.105.90.153:49776',
'http://123.160.51.139:36100',
'http://123.163.178.31:46538',
'http://222.188.200.197:39891',
'http://218.58.234.167:31893',
'http://183.32.143.11:32347',
'http://49.69.216.198:41567',
'http://27.153.16.7:28205',
'http://220.186.159.194:33358',
'http://1.197.57.255:29036',
'http://123.134.98.55:42496',
'http://218.58.248.254:45195',
'http://124.132.114.143:44832',
'http://1.199.195.179:36756',
'http://116.53.197.84:49999',
'http://36.22.77.63:25264',
'http://49.70.33.218:23900',
'http://123.149.163.47:39904',
'http://114.107.5.93:29039',
'http://113.101.252.146:23896',
'http://222.188.182.46:36541',
'http://117.63.11.210:39914',
'http://183.154.53.111:24999',
'http://125.109.198.44:25912',
'http://124.113.216.96:49927',
'http://117.26.231.17:20995',
'http://114.232.119.56:20832',
'http://123.101.165.40:37719',
'http://113.103.121.107:31697',
'http://60.175.213.45:36164',
'http://115.207.2.243:31839',
'http://106.111.247.3:30753',
'http://60.169.127.57:22701',
'http://49.77.208.110:29447',
'http://124.113.216.191:41005',
'http://116.115.211.207:26423',
'http://27.204.4.103:30240',
'http://106.110.0.19:29086',
'http://49.76.125.105:26938',
'http://60.169.219.76:24539',
'http://182.38.74.229:33300',
'http://1.193.192.76:20989',
'http://101.27.20.116:32450',
'http://171.12.183.57:29202',
'http://180.122.151.74:35746',
'http://222.172.139.226:47950',
'http://112.195.205.133:35487',
'http://60.182.79.33:29982',
'http://117.26.89.179:32672',
'http://125.123.123.64:24758',
'http://115.221.126.243:26174',
'http://60.169.126.132:46251',
'http://115.213.225.38:33079',
'http://125.78.16.53:25892',
'http://114.226.68.6:49154',
'http://220.186.187.100:47026',
'http://125.123.120.10:31528',
'http://112.192.253.16:25581',
'http://114.232.107.243:46408',
'http://183.188.241.237:41756',
'http://60.175.213.86:28729',
'http://115.203.182.52:36019',
'http://113.128.25.243:29325',
'http://117.57.90.104:33786',
'http://117.67.131.20:42452',
'http://220.161.242.51:41244',
'http://59.60.123.108:37368',
'http://117.67.142.192:25954',
'http://123.161.157.55:46816',
'http://36.24.41.114:44444',
'http://49.76.55.155:33195',
'http://114.222.129.29:44976',
'http://49.81.9.209:27134',
'http://182.202.223.121:34654',
'http://115.209.181.112:44019',
'http://183.32.216.66:44900',
'http://119.138.195.64:34140',
'http://218.13.226.163:37365',
'http://183.32.219.138:28002',
'http://113.94.123.194:47274',
'http://14.115.71.217:24109',
'http://1.192.138.231:49156',
'http://115.208.10.80:29003',
'http://123.52.49.176:25588',
'http://106.110.86.114:26639',
'http://182.127.81.5:48950',
'http://223.215.103.4:45336',
'http://114.235.166.119:48503',
'http://49.75.159.233:32421',
'http://183.143.116.155:47477',
'http://114.227.206.21:40515',
'http://114.239.172.224:47746',
'http://117.57.21.58:24894',
'http://110.18.153.142:30736',
'http://221.225.113.60:39173',
'http://114.99.5.80:21487',
'http://49.84.196.248:29141',
'http://112.192.248.231:40514',
'http://182.38.91.149:37783',
'http://121.234.244.52:23918',
'http://222.172.139.248:49400',
'http://116.208.98.61:28029',
'http://183.142.154.80:34249',
'http://114.236.25.202:39701',
'http://49.85.29.15:31788',
'http://180.117.127.163:25632',
'http://117.57.90.32:30564',
'http://117.86.34.189:38397',
'http://220.179.219.99:24768',
'http://101.27.20.134:29475',
'http://49.65.160.119:40024',
'http://60.31.89.187:48240',
'http://1.31.96.186:30533',
'http://36.57.87.173:25531',
'http://113.121.168.47:39849',
'http://115.203.213.162:28029',
'http://60.173.24.231:20689']

class WeixinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class ProxyMiddleware():
	def __init__(self, proxy_url):
		self.logger = logging.getLogger(__name__)
		self.proxy_url = proxy_url
	
	def get_random_proxy(self):
		r = random.randint(0, len(agents)-1)
		return agents[r]
	def process_request(self, request, spider):
		print('------------------------------------------------------------------')
		print(request.meta.get('retry_times'))
		#if request.meta.get('retry_times'):
	
		proxy = self.get_random_proxy()
				
		uri = proxy
		self.logger.debug('using hte agent: ' + proxy)
		request.meta['proxy'] = uri
			
	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		r = random.randint(0, len(agents)-1)
		s = cls(agents[r])
		
		return s
	
class WeixinDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
