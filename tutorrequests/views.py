from django.shortcuts import render
from request_help.models import HelpRequest
# import googlemaps
from datetime import datetime
import googlemaps
from tuber.settings import GOOGLE_MAPS_API_KEY


def home(request):
    context = {
        'requests': HelpRequest.objects.all()
    }
    return render(request, 'tutorrequests/requests_home.html', context)


def details(request, pk):
    req = HelpRequest.objects.get(pk=pk)
    
    loc = str(req.location)
    print(loc)
    locations = {
        'clem': '164 McCormick Rd, Charlottesville, VA 22903',
        'Clark Library': '291 McCormick Rd, Charlottesville, VA 22903',
        'Alderman Library': '160 McCormick Rd, Charlottesville, VA 22904',
        'Music Library': 'Cabell Dr L001, Charlottesville, VA 22904',
        'Rice Hall': '5 Engineer\'s Way, Charlottesville, VA 22903',
    }

    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    student_location = locations.get(loc)
    tutor_location = locations.get('Alderman Library')
    now = datetime.now()
    print(student_location, tutor_location)
    directions_result = gmaps.directions(student_location, tutor_location, mode="walking", departure_time="now")
    walking = directions_result[0]['legs']
    directions_distance = walking[0]['distance']
    directions_duration = walking[0]['duration']
    
    context = {
        'request': req,
        'start' : tutor_location,
        'end' : student_location,
        'distance' : directions_distance,
        'duration' : directions_duration,
    }
    return render(request, 'tutorrequests/requests_detail.html', context)