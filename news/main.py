import os
import sys

from scrapy import cmdline

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# cmdline.execute('scrapy crawl GaoxinBendiDongtai'.split(' '))
cmdline.execute('scrapy crawl test1'.split(' '))
