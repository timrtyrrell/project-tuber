from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Locations

@admin.register(Locations)
class LocationsAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')