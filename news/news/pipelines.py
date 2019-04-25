# -*- coding: utf-8 -*-
import pymongo
import os

from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline
from news.items import NewsItem
from news.settings import POLICY_TYPE, INDUSTRY, DEPARTMENT


class DownloadFilesPipeline(FilesPipeline):
    """自定义图片名称"""
    def get_media_requests(self, item, info):
        return [Request(x, meta={'item': item}) for x in item.get(self.files_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('FilesPipeline.file_key(url) method is deprecated, please use '
                          'file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        item = request.meta['item']
        folder_name = item['infoSource']
        file_name = item['file_name']
        return '%s/%s' % (folder_name, file_name)


class ProcessorFiledPipeline(object):
    """删除file_name"""
    def process_item(self, item, spider):
        return item
        # if item.get('file_name'):
        #     del item['file_name']
        # return item

class NewsPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_settings(cls, settings):
        return cls(mongo_uri=settings.get('MONGO_URI'), mongo_db=settings.get('MONGO_DB')
                   )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[NewsItem.collection]
        print(self.collection.count())
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, NewsItem):
            item = dict(item)
            # self.collection.insert(item)
            self.collection.update(item, {'$set': item}, True)