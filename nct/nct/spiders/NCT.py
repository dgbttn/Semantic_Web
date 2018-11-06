# -*- coding: utf-8 -*-

import scrapy, requests, csv, time


class NCTSpider(scrapy.Spider):
    name = 'nct'

    allowed_domains = ['www.nhaccuatui.com']
    start_urls = []

    with open('artists.csv') as File:
        reader = csv.reader(File)
        links = next(zip(*reader))

    print('import csv done')

    output = []

    for link in links:
        output.append('##### NEW FILE #####')
        output.append(link)
        try:
            req = requests.get(link)
        except requests.exceptions.ConnectionError:
            time.sleep(2)
            print('retry', link)
            req = requests.get(link)
        if req.ok:
            output.append(req.text)
        else:
            print(link)

    print('crawl done')

    with open('nct_artists.txt', 'w', encoding='utf8') as f:
        f.write('\n'.join(output))

    print('write done')

