# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItemLoader, NewsItem
# from news.settings import SAVE_TIME
from news.utils import get_config
from news.rules import *


class NbhtzSpider(scrapy.Spider):
    name = 'Universal'

    def __init__(self, name, *args, **kwargs):
        self.config = get_config(name)
        self.allowed_domains = self.config['allowed_domains']
        self.start_urls = self.config.get('start_urls')
        if self.config.get('url'):
            self.url = self.config.get('url')
        self.request = eval(self.config.get('rules'))
        self.data = self.config.get('data')
        if self.data:
            self.post_data = self.data
        super(NbhtzSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for url in self.start_urls:
            if self.data:
                yield FormRequest(url=url, formdata=self.post_data, callback=self.parse, dont_filter=True)
            else:
                yield Request(url=url, dont_filter=True)

    def parse(self, response):
        for req_item in self.request(self, response):
            yield req_item

    def parse_detail(self, response):
        item = self.config.get('item')
        if item:
            # 加载item和item_loader
            item_cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(item=item_cls, response=response)
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor['method'] == 'css':
                        loader.add_css(key, *extractor['args'],  **{'re': extractor.get('re')})
                    if extractor['method'] == 'xpath':
                        loader.add_xpath(key, *extractor['args'], **{'re': extractor.get('re')})
                    if extractor['method'] == 'value':
                        loader.add_value(key, *extractor['args'], **{'re': extractor.get('re')})
                    if extractor['method'] == 'attr':
                        loader.add_value(key, getattr(response, *extractor['args']))
                    if extractor['method'] == 'file:css':
                        if extractor.get('re'):
                            urls = response.css(*extractor['args']).re(extractor['re'])
                        else:
                            urls = response.css(*extractor['args']).extract()
                        file_urls = [response.urljoin(url) for url in urls]
                        loader.add_value(key, file_urls)
            news_item = loader.load_item()
            yield news_item

