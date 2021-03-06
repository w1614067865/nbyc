import sys

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from news.utils import get_config


def run():
    # name = sys.argv[1]
    name = 'gaoxinzhengce'
    custom_settings = get_config(name)
    spider = custom_settings.get('spider')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    custom_settings.get('settings')
    process = CrawlerProcess(settings)
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()