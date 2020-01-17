from django.contrib import admin
from .models import PinLocation, County
from django.contrib.gis.admin import OSMGeoAdmin

class PinLocationAdmin(OSMGeoAdmin):
    list_display = ('title','date_reported','location')
    search_fields = ('title',)
    filter_fields = ('title','date_reported')

class CountyAdmin(OSMGeoAdmin):
    list_display = ('name', 'gemeinde_n', 'land_name')
    search_fields = ('name', 'gemeinde_n')
    filter_fields = ('name')



admin.site.register(PinLocation, PinLocationAdmin)
admin.site.register(County, CountyAdmin)
