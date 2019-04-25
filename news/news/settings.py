# -*- coding: utf-8 -*-
import time
import os
import sys

# 添加搜索路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_PATH)

BOT_NAME = 'news'

SPIDER_MODULES = ['news.spiders']
NEWSPIDER_MODULE = 'news.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'news.middlewares.NewsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'news.middlewares.NewsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'news.pipelines.NewsPipeline': 300,
    'news.pipelines.MongoDBPipeline': 300,
    'scrapy.pipelines.files.FilesPipeline': 1,
    # 'news.pipelines.DownloadFilesPipeline': 1,
    # 'news.pipelines.ProcessorFiledPipeline': 100,

}

FILES_STORE = BASE_PATH + '/Download'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# scrapy_redis调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# scrapy_redis去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 配置redis
REDIS_URL = 'redis://localhost:6379'

# BoolFilter调度器
SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"
# BoolFilter过滤器
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
# BoolFilter生成的hash函数的个数
BLOOMFILTER_HASH_NUMBER = 6
# BoolFilter位数组大小 2 * 30次方， 约暂用redis内存128M
BLOOMFILTER_BIT = 30

# redis持久化
SCHEDULER_PERSIST = True
# scrapy_redis or BoolFilter重爬
SCHEDULER_FLUSH_ON_START = True


# 配置mongodb
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = 'NingoGaoxin'

# 政策类型
POLICY_TYPE = {'政策通知': '2', '政策要闻': '3', '政策文件': '4', '政策解读': '5'}
# 部门类型
DEPARTMENT = {'人民政府': '1', '发展改革': '2', '科技部门': '3', '工业经信': '4', '财政税务': '5', '商务海关': '6', '工商质监': '7', '组织人社': '8', '文化广电': '9', '规划统计': '10', '其他部门': '11', '知识产权': '13', '高新区': '14', '经开区': '15'}
# 判断是否为新记录，后期使用  默认：1
NEW_RECORD = 1
# 技术领域(行业) 默认
INDUSTRY = ',2,3,4,5,6,7,8,9,10,11,12,'
# 街道 默认值为0
BOROUGH = '0'
# 区县
DOWNTOWN = '0'
# 城市
CITYE = '330200'
# 省份
PROVINCE = '330000'
ISMARK = '0'
RSID = '0'
# 发布机构
RELEASEORGANIZATION = '宁波'
# 记录最后更新时间，修改爬虫返回的数据
LASTUPDATE = '0'
