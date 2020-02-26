from django.shortcuts import render
import googlemaps
from datetime import datetime

# Create your views here.

def index(request):
    gmaps = googlemaps.Client(key='AIzaSyDJ3OMK3ABdQ76t7u0y6yB6XaL0XMTYXN4')
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
    return render(request, 'geodjango/index.html')