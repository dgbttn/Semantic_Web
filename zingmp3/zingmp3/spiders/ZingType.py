# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
import csv

class ZingSpider(CrawlSpider):
    name = 'ZingType'

    start_urls = []

    with open("type_links.csv", encoding = 'utf8') as f:
        reader = csv.reader(f)
        reader = list(reader)[2:] 
        for row in reader :
            if len(row)>0 : 
                start_urls.append(row[0])


    def parse(self, response):
        domain = 'mp3.zing.vn'
        type = response.css("h2.title-section::text").extract_first()
        artists = response.css("h3.name-item.fw7.ellipsis")
        artistNum = len(artists)
        for i in range(artistNum):
            artistName = artists[i].css("a::text").extract_first()
            url = domain + artists[i].css("a::attr(href)").extract_first()
            yield {
                'type' : type,
                'name' : artistName,
                'url' : url
            }

    


