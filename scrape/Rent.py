#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.crawler import CrawlerProcess
import re

results = []
districts_rent = {
'Charlottenburg-Wilmersdorf': (0,0),
'Friedrichshain-Kreuzberg': (0,0),
'Tempelhof-Schöneberg': (0,0),
'Lichtenberg': (0,0),
'Marzahn-Hellersdorf': (0,0),
'Mitte': (0,0),
'Neukölln': (0,0),
'Pankow': (0,0),
'Treptow-Köpenick': (0,0),
'Prenzlauer Berg': (0,0),
'Spandau': (0,0),
'Reinickendorf': (0,0),
'Steglitz-Zehlendorf': (0,0)
}

class Rent:
    def __init__(self, district, rent):
        print(district, rent)
        self.district = district
        if rent is None or rent == "":
            self.rent = 0
        else:
            self.rent = rent

class ParkSpider(scrapy.Spider):
    name = 'Rent'
    allowed_domains = ['www.wohnungsboerse.net']
    start_urls = ['https://www.wohnungsboerse.net/mietspiegel-Berlin/2825']

    def parse(self, response):
        global results
        regex_district = '(.*)'
        tables = response.css('table.rentindexDistrict_table')[:2]
        for table in tables:
            table_data = table.css('tbody')
            for row in table_data.css('tr'):
                tds = row.css('td')
                dis = tds[0].css('::text').get()
                match = re.search('\(.*\)', dis)
                if match is None:
                    continue
                #else: print(dis[match.span()[0]:match.span()[1]])
                dis = dis[match.span()[0]:match.span()[1]].replace('(', '')
                dis = dis.replace(')','')
                rent = float(tds[1].css('::text').get().strip().strip('€').strip('\xa0').replace(',','.'))
                for key, value in districts_rent.items():
                    if dis in key:
                        old = districts_rent[key]
                        new = (old[0] + rent, old[1]+1)
                        districts_rent[key] = new




if __name__ == '__main__':
    process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json'
})
    process.crawl(ParkSpider)
    process.start() # the script will block here until the crawling is
    print(districts_rent)

    with open('rent.csv','w') as f:
        f.write('district,rent\n')
        for key, value in districts_rent.items():
            f.write(f'{key},{value[0]/value[1]}\n')
