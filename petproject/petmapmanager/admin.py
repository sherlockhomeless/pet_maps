from django.contrib import admin
from .models import Location, County, Animal
from leaflet.admin import LeafletGeoAdmin


class LocationAdmin(LeafletGeoAdmin):
    list_display = ('title', 'date_reported','location')
    search_fields = ('title',)
    filter_fields = ('title', 'date_reported')


class CountyAdmin(LeafletGeoAdmin):
    list_display = ('name', 'gemeinde_n','gemeinde_s')
    search_fields = ('name',)
    filter_fields = ('name', 'gemeinde_s')


class AnimalAdmin(LeafletGeoAdmin):
    list_display = ('ort', 'display_na', 'latlong')
    search_fields = ('ort', 'display_na')
    filter_fields = ('ort', 'display_na', 'latlong')


admin.site.register(Location, LocationAdmin)

admin.site.register(County, CountyAdmin)

admin.site.register(Animal, AnimalAdmin)