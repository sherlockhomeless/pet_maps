#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

results = []
results = []
districts_dens = {
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

class Density:
    def __init__(self, district, density):
        self.district = district
        print(density)
        if density is None or density is "":
            self.density = 0
        else:
            self.density = density

        def __str__(self):
            #return str((self.district, self.density))
            return "bla"

class DensitySpider(scrapy.Spider):
    name = 'DensitySpider'
    allowed_domains = ['de.wikipedia.org']
    start_urls = ['https://de.wikipedia.org/wiki/Verwaltungsgliederung_Berlins']

    def parse(self, response):
        global results
        table = response.css('tbody')[1]
        rows = table.css('tr')
        print('###### START ######')
        for i, row in enumerate(rows):
            dis, dens = None, None
            for j,td in enumerate(row.css('td')):
                if j == 1: # bezirk
                    dis = td.css('::text').get()
                elif j == 5: # einwohner pro km²
                    dens = td.css('::text').getall()
                    if len(dens) > 1:
                        dens = dens[1]
                    else:
                        dens = dens[0]
            new_dens = Density(dis, dens)
            results.append(new_dens)

        print('##### END #####')

if __name__ == '__main__':
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(DensitySpider)
    process.start()

    for el in results:
        if el.district is None:
            continue
        else:
            districts_dens[el.district] = el.density

    with open('density.csv', 'w') as f:
        f.write('district,density\n')
        for key, value in districts_dens.items():
            f.write(f'{key},{value}')
