# Create your models here.
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager


# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=250, null=True)
    date_reported = models.DateField(auto_now_add=True)
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "locations"


class County(models.Model):
    gml_id = models.CharField(max_length=80)
    gemeinde_n = models.CharField(max_length=80)
    gemeinde_s = models.CharField(max_length=80)
    land_name = models.CharField(max_length=80)
    land_schlu = models.CharField(max_length=80)
    schluessel = models.CharField(max_length=80)
    name = models.CharField(max_length=254)
    animal_cou = models.CharField(max_length=254)
    district = models.CharField(max_length=254)
    parksize = models.CharField(max_length=254)
    density = models.CharField(max_length=254)
    rent = models.CharField(max_length=254)
    countyid = models.BigIntegerField(primary_key=True)
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.gemeinde_n

    class Meta:
        verbose_name_plural = "counties"

class Animal(models.Model):
    #strasse = models.CharField(max_length=31, default=None)
    land = models.CharField(max_length=7)
    #plz = models.CharField(max_length=6)
    ort = models.CharField(max_length=27)
    result_num = models.CharField(max_length=1)
    osm_id = models.CharField(max_length=10)
    display_na = models.CharField(max_length=151)
    category = models.CharField(max_length=8)
    type = models.CharField(max_length=18)
    latlong = models.CharField(max_length=37)
    geom = gis_models.PointField(srid=4326)

    def __str__(self):
        return self.latlong

    class Meta:
        verbose_name_plural = "animals"
