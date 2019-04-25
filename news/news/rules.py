from scrapy import FormRequest
from scrapy.selector import Selector
from scrapy.http import Request


def gaoxin_parse(self, response):
    if 'startrecord=1&endrecord=120' in response.url:
        # item总数量
        total_items = int(response.xpath('//totalrecord/text()').extract_first())
        # url总页数
        total_page = int(response.xpath('//totalpage/text()').extract_first())
        request_num = total_page // 3 + 1
        for url in map(lambda num: self.url.format(num * 120 + 1, num * 120 + 120), range(1, request_num)):
            yield FormRequest(url=url, formdata=self.post_data)

    items = response.xpath('//recordset//record/text()').extract()
    html = ' '.join(items)
    sel = Selector(text=html)
    for link in sel.xpath('//*[@class="bt_link"]/@href').extract():
        url = response.urljoin(link)
        yield Request(url, callback=self.parse_detail)
