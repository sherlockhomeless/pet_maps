import os
from django.contrib.gis.utils import LayerMapping
from .models import County, Animal


# Auto-generated `LayerMapping` dictionary for County model
county_mapping = {
    'gml_id': 'gml_id',
    'gemeinde_n': 'Gemeinde_n',
    'gemeinde_s': 'Gemeinde_s',
    'land_name': 'Land_name',
    'land_schlu': 'Land_schlu',
    'schluessel': 'Schluessel',
    'name': 'Name',
    'animal_cou': 'Animal_Cou',
    'district': 'District',
    'parksize': 'Parksize',
    'density': 'Density',
    'rent': 'Rent',
    'countyid': 'countyID',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for Animal model
animal_mapping = {
    #'strasse': 'Strasse',
    'land': 'Land',
    #'plz': 'PLZ',
    'ort': 'Ort',
    'result_num': 'result_num',
    'osm_id': 'osm_id',
    'display_na': 'display_na',
    'category': 'category',
    'type': 'type',
    'latlong': 'latlong',
    'geom': 'POINT',
}


county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/finalshapefile', 'finalBerlinReal.shp'),)

animal_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/animalsBerlinGeoJSON', 'berlinGeoJSON.shp'),)


def run(verbose=True):
    lm = LayerMapping(County, county_shp, county_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def run1(verbose=True):
    lm1 = LayerMapping(Animal, animal_shp, animal_mapping, transform=False, encoding='iso-8859-1')
    lm1.save(strict=True, verbose=verbose)
