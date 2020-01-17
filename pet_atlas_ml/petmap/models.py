from django.db import models

from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager

class PinLocation(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=250, null=True)
    date_reported = models.DateField(auto_now_add=True)
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = " PinLocation"



class County(models.Model):
    gml_id = models.CharField(max_length=80)
    gemeinde_n = models.CharField(max_length=80)
    gemeinde_s = models.CharField(max_length=80)
    land_name = models.CharField(max_length=80)
    land_schlu = models.CharField(max_length=80)
    schluessel = models.CharField(max_length=80)
    gem_s = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    animal_cou = models.CharField(max_length=254)
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.gemeinde_n

    class Meta:
        verbose_name_plural = " County"
