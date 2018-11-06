import csv
from scrapy.spiders import CrawlSpider

class testCrawler(CrawlSpider):
	name = 'count'

	start_urls = []

	with open("types.csv", encoding = 'utf8') as f:
		reader = csv.reader(f)
		reader = list(reader)[2:] 
		for row in reader :
			if len(row)>1 : 
				start_urls.append("http://mp3.zing.vn" + row[2])

	def parse(self, response) :
		page_sep = "?&page="
		url = response.url
		bar = response.css("div.pagination")
		if len(bar) == 0:
			link = url + page_sep + str(1)
			# print(link)
			yield {'link' : link}
		else :
			pages = bar.css("a::attr(href)").extract()
			pageNum = int(pages[len(pages)-1].split("page=")[-1])
			for i in range(pageNum) : 
				link = url + page_sep + str(i+1)
				# print(link)	
				yield {'link' : link}