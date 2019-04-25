# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Test1Spider(CrawlSpider):
    name = 'test1'
    allowed_domains = ['www.nbhtz.gov.cn']
    start_urls = ['http://www.nbhtz.gov.cn/']
    post_data = {'col': '1', 'webid': '140', 'path': '/', 'columnid': '81953', 'sourceContentType': '1', 'unitid': '129165', 'webname': '宁波国家高新区宁波新材料科技城', 'permissiontype': '0'}

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        url = 'http://www.nbhtz.gov.cn/module/web/jpage/dataproxy.jsp?startrecord=1&endrecord=120&perpage=40'
        yield scrapy.FormRequest(url=url, formdata=self.post_data)

    def parse_start_url(self, response):
        pass

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
