# -*- coding: utf-8 -*-
import scrapy


class GaoxintongzhigonggaoSpider(scrapy.Spider):
    name = 'GaoxinTongzhiGongGao'
    allowed_domains = ['www.nbhtz.gov.cn']
    start_urls = ['http://www.nbhtz.gov.cn/']

    def parse(self, response):
        pass

