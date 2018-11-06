
from scrapy.spiders import CrawlSpider

class testCrawler(CrawlSpider):
	name = 'test'

	allowed_domains = ['mp3.zing.vn']

	start_urls = []

	for page in range(1,18) :
		link = 'https://mp3.zing.vn/the-loai-nghe-si/Nhac-Tre/IWZ9Z088.html' + '?&page=' + str(page)
		start_urls.append(link)

	def parse(self, response) :

		artistNames = []

		artists = response.css("div.pone-of-five.artist-item")                                 

		for artist in artists:
			name = artist.css("h3.name-item.fw7.ellipsis a::text")[0].extract()
			artistNames.append(name)

		with open("artists.txt", "a", encoding = 'utf8') as file:
			file.write('\n'.join(artistNames))