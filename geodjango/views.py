from django.shortcuts import render
import googlemaps
from datetime import datetime

from tuber.settings import GOOGLE_MAPS_API_KEY

# Create your views here.

def index(request):
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    clark_hall = '291 McCormick Rd, Charlottesville, VA 22903'
    alderman_library = '160 McCormick Rd, Charlottesville, VA 22904'


    now = datetime.now()
    tutor_address = str(request.POST.get('address_input', False))
    directions_result = ''
    if tutor_address != '':
        directions_result = gmaps.directions(tutor_address,
                                        alderman_library,
                                        mode="walking",
                                        departure_time=now)
    '''
    directions_result = gmaps.directions(clark_hall,
                                     alderman_library,
                                     mode="walking",
                                     departure_time=now)
    '''

    walking = directions_result[0]['legs']
    directions_distance = walking[0]['distance']
    print(directions_result[0])
    directions_duration = walking[0]['duration']
    test_instruct = walking[0]['steps'][0]['html_instructions']


    context = {
        'start' : clark_hall,
        'end' : alderman_library,
        'distance' : directions_distance,
        'duration' : directions_duration,
    }
    return render(request, 'geodjango/index.html', context)