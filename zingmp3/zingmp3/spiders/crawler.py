import requests
from scrapy.spiders import CrawlSpider

class crawler(CrawlSpider):
    name = 'crawler'

    start_urls = []
    link = 'https://mp3.zing.vn/the-loai-nghe-si/Nhac-Tre/IWZ9Z088.html?&page=1'

    with open('zingart1.html', "w", encoding = 'utf8') as f:
    	req = requests.get(link)
    	f.write(req.text)