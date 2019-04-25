# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from news.items import NewsItemLoader, NewsItem
# from news.settings import SAVE_TIME


class NbhtzSpider(scrapy.Spider):
    """宁波高新区本地动态页"""
    name = 'GaoxinBendiDongtai'
    allowed_domains = ['www.nbhtz.gov.cn']
    url = 'http://www.nbhtz.gov.cn/module/web/jpage/dataproxy.jsp?startrecord={0}&endrecord={1}&perpage=40'
    post_data = {'col': '1', 'webid': '140', 'path': '/', 'columnid': '81953', 'sourceContentType': '1', 'unitid': '129165', 'webname': '宁波国家高新区宁波新材料科技城', 'permissiontype': '0'}
    # post_data = {'col': '1', 'webid': '140', 'path': '/', 'columnid': '81952', 'sourceContentType': '1', 'unitid': '129165', 'webname': '宁波国家高新区宁波新材料科技城', 'permissiontype': '0'}

    def start_requests(self):
        url = 'http://www.nbhtz.gov.cn/module/web/jpage/dataproxy.jsp?startrecord=1&endrecord=120&perpage=40'
        yield scrapy.FormRequest(url=url, formdata=self.post_data, callback=self.parse)

    def parse(self, response):
        # print(response.url)
        if 'startrecord=1&endrecord=120' in response.url:
            # item总数量
            total_items = int(response.xpath('//totalrecord/text()').extract_first())
            # url总页数
            total_page = int(response.xpath('//totalpage/text()').extract_first())
            request_num = total_page // 3 + 1
            for url in map(self.build_url, range(1, request_num)):
                print(url)
                yield scrapy.FormRequest(url=url, formdata=self.post_data)

        items = response.xpath('//recordset//record/text()').extract()
        html = ' '.join(items)
        sel = Selector(text=html)
        for link in sel.xpath('//*[@class="bt_link"]/@href').extract():
            url = response.urljoin(link)
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        item_loader = NewsItemLoader(item=NewsItem(), response=response)
        print(response.url)
        item_loader.add_value('id', response.url)
        item_loader.add_css('title', '#detail>h2::text')
        item_loader.add_xpath('time', '//*[@id="detail"]/div[@class="d_info"]/span[1]/text()')
        item_loader.add_css('content', '#zoom')
        item_loader.add_value('savetime', SAVE_TIME())
        item_loader.add_value('releaseOrganization', ' ')
        item_loader.add_value('province', ' ')
        item_loader.add_value('citye', ' ')
        item_loader.add_value('downtown', ' ')
        item_loader.add_value('borough', ' ')
        item_loader.add_value('lastupdate', ' ')
        item_loader.add_value('newRecord', '')
        item_loader.add_value('rsid', ' ')
        item_loader.add_value('policytype', '')
        item_loader.add_value('department', '')
        item_loader.add_value('industry', '')
        item_loader.add_value('isMark', 0)
        item_loader.add_value('infoSource', '宁波高新区本地动态')
        # item_loader.add_value('infoSource', '宁波高新区通知公告')
        item = item_loader.load_item()
        # print(item)
        yield item

    def build_url(self, num):
            # 构建url地址
            request_count = num * 120
            return self.url.format(request_count+1, request_count + 120)

