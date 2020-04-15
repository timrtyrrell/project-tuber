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
    not_tutor = True

    if request.user.userprofile.status == False:
        other = 'aldy'
    else:
        other = request.user.userprofile.tutor_location
        not_tutor = False
    
    loc = str(req.location)
    other = str(other)

    locations = {
        'clem': '164 McCormick Rd, Charlottesville, VA 22903',
        'clark': '291 McCormick Rd, Charlottesville, VA 22903',
        'aldy': '160 McCormick Rd, Charlottesville, VA 22904',
        'music': 'Cabell Dr L001, Charlottesville, VA 22904',
        'rice': '5 Engineer\'s Way, Charlottesville, VA 22903',
    }

    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    student_location = locations.get(loc)
    tutor_location = locations.get(other)
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
        'not_tutor': not_tutor,
    }
    return render(request, 'tutorrequests/requests_detail.html', context)