import os
from django.contrib.gis.utils import LayerMapping
from .models import County

# Auto-generated `LayerMapping` dictionary for County model
county_mapping = {
    'gml_id': 'gml_id',
    'gemeinde_n': 'Gemeinde_n',
    'gemeinde_s': 'Gemeinde_s',
    'land_name': 'Land_name',
    'land_schlu': 'Land_schlu',
    'schluessel': 'Schluessel',
    'gem_s': 'gem_s',
    'name': 'Name',
    'animal_cou': 'Animal_Cou',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'berlinsbezirkstiere.shp'),)

def run(verbose=True):
    lm = LayerMapping(County, county_shp, county_mapping, transform= False, encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)
