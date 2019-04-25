import re
import time

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose
# from news.settings import POLICY_TYPE, INDUSTRY, DEPARTMENT, NEW_RECORD, BOROUGH, DOWNTOWN, CITYE, PROVINCE, ISMARK,RSID, RELEASEORGANIZATION
from news.settings import *


def delete_blank(value):
    if isinstance(value, list):
        value = ''.join(value)
    value = re.sub(r'\s', '', value)
    return value

def filter_time(value):
    if re.match(r'.*?(\d+.*)', value):
        value = re.match(r'.*?(\d+.*)', value).group(1)
        return value
    return value

def delete_html(value):
    """删除html标签"""
    pass

def save_time(value):
    if not value:
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return value


class NewsItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class NewsItem(Item):
    collection = 'test2'
    _id = Field()
    title = Field(input_processor=Compose(delete_blank))
    content = Field()
    time = Field(input_processor=MapCompose(filter_time))
    policytype = Field(input_processor=MapCompose(lambda s: s if s else POLICY_TYPE['政策要闻']))
    department = Field(input_processor=MapCompose(lambda s: s if s else DEPARTMENT['人民政府']))
    industry = Field(input_processor=MapCompose(lambda s: s if s else INDUSTRY))
    releaseOrganization = Field(input_processor=MapCompose(lambda s: s if s else RELEASEORGANIZATION))
    province = Field(input_processor=MapCompose(lambda s: s if s else PROVINCE))
    citye = Field(input_processor=MapCompose(lambda s: s if s else CITYE))
    downtown = Field(input_processor=MapCompose(lambda s: s if s else DOWNTOWN))
    borough = Field(input_processor=MapCompose(lambda s: s if s else BOROUGH))
    lastupdate = Field(input_processor=MapCompose(lambda s: s if s else LASTUPDATE))
    savetime = Field(input_processor=MapCompose(save_time))
    newRecord = Field(input_processor=MapCompose(lambda i: i if i else NEW_RECORD))
    rsid = Field(input_processor=MapCompose(lambda i: i if i else RSID))
    isMark = Field(input_processor=MapCompose(lambda s: s if s else ISMARK))
    infoSource = Field()

    # 下载文件
    file_urls = Field(output_processor=MapCompose(lambda s: s))
    files = Field()