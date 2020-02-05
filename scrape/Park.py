#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.crawler import CrawlerProcess

results = []
districts_size = {
'Charlottenburg-Wilmersdorf': 0,
'Friedrichshain-Kreuzberg': 0,
'Tempelhof-Schöneberg': 0,
'Lichtenberg': 0,
'Marzahn-Hellersdorf': 0,
'Mitte': 0,
'Neukölln': 0,
'Pankow': 0,
'Treptow-Köpenick': 0,
'Prenzlauer Berg': 0,
'Spandau': 0,
'Reinickendorf': 0,
'Steglitz-Zehlendorf': 0
}

class Park:
    def __init__(self, district, neighbourhood, size):
        print(district, neighbourhood, size)
        self.district = district
        self.neighbourhood = neighbourhood
        if size is None or size == "":
            self.size = 0
        else:
            self.size = size

    def is_valid_park(self):
        return self.size != 0 and self.district is not None and self.neighbourhood is not None

class ParkSpider(scrapy.Spider):
    name = 'Park'
    allowed_domains = ['de.wikipedia.org/wiki/Liste_von_Parkanlagen_in_Berlin']
    start_urls = ['http://de.wikipedia.org/wiki/Liste_von_Parkanlagen_in_Berlin']

    def parse(self, response):
        global results
        table_data = response.css('tbody')
        table_rows = table_data.css('tr')
        for row in table_rows:
            dis, nei, size = None, None, None
            for i, td in enumerate(row.css('td')):
                td = td.css('::text').get()
                #print(i, td)
                if i == 1: # Bezirk
                    dis = td
                if i == 2: # Ortsteil
                    nei = td
                if i == 3: # Größe
                    size = td
            results.append(Park(dis, nei, size))


if __name__ == '__main__':
    process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json'
})
    process.crawl(ParkSpider)
    process.start() # the script will block here until the crawling is finished
    #print("length, example", len(results), results[0].district, results[1].neighbourhood, results[1].size)

    for park in results:
        if park.is_valid_park():
            if park.district in districts_size:
                districts_size[park.district] += float(park.size)

    with open('parks.csv', 'w') as f:
        f.write('district,parksize\n')
        for key, value in districts_size.items():
            f.write(f'{key},{value}\n')
