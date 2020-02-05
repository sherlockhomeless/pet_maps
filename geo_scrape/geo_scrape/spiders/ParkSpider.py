#!/usr/bin/env python3


# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

results = []

class Park:
    def __init__(self, district, neighbourhood, size):
        self.district = district
        self.neighbourhood = neighbourhood
        if size is None or size is "":
            self.size = 0
        else:
            self.size = size

        def __str__(self):
            return (self.district, self.neighbourhood, self.size)

        def __repr__(self):
            return (self.district, self.neighbourhood, self.size)

class ParkspiderSpider(scrapy.Spider):
    name = 'ParkSpider'
    allowed_domains = ['de.wikipedia.org/wiki/Liste_von_Parkanlagen_in_Berlin']
    start_urls = ['https://de.wikipedia.org/wiki/Liste_von_Parkanlagen_in_Berlin']

    def parse(self, response):
        global results
        table = response.css('tbody')
        rows = table.css('tr')
        print('###### START ######')
        for i, row in enumerate(rows):
            dis, nei, size = None, None, None
            for j,td in enumerate(row.css('td')):
                if j == 1: # bezirk
                    dis = td.css('::text').get()
                elif j == 2: # ortsteil
                    nei = td.css('::text').get()
                elif j == 3: # größe in ha
                    size = td.css('::text').get()
            new_park = Park(dis, nei, size)
            print(new_park)

        print('##### END #####')

if __name__ == '__main__':
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(ParkspiderSpider)
    process.start()
