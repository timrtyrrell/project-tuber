from django.shortcuts import render
import googlemaps
from datetime import datetime

from tuber.settings import GOOGLE_MAPS_API_KEY

# Create your views here.

def index(request):
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    now = datetime.now()
    '''
    directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
    '''
    print(reverse_geocode_result)
    return render(request, 'geodjango/index.html')