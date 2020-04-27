from django.shortcuts import render
from request_help.models import HelpRequest
from datetime import datetime
import googlemaps
from tuber.settings import GOOGLE_MAPS_API_KEY

from register.models import UserProfile

def home(request):
    context = {
        'requests': HelpRequest.objects.all()
    }
    return render(request, 'tutorrequests/requests_home.html', context)

def delete(request, pk):
    HelpRequest.objects.filter(pk=pk).delete()
    context = {
        'requests': HelpRequest.objects.all()
    }
    return render(request, 'tutorrequests/requests_home.html', context)


def details(request, pk):
    req = HelpRequest.objects.get(pk=pk)
    other = 'rice'
    if (UserProfile.objects.filter(user=request.user).exists()):
        other = request.user.userprofile.tutor_location
    student_name = req.user.name
    student_phone = req.user.phone
    loc = str(req.location)
    print("this is the ", loc, other)
    locations = {
        'Clemons Library': '164 McCormick Rd, Charlottesville, VA 22903',
        'Clark Library': '291 McCormick Rd, Charlottesville, VA 22903',
        'Alderman Library': '160 McCormick Rd, Charlottesville, VA 22904',
        'Music Library': 'Cabell Dr L001, Charlottesville, VA 22904',
        'Rice Hall': '5 Engineer\'s Way, Charlottesville, VA 22903',
    }
    locations2 = {
        'clem': '164 McCormick Rd, Charlottesville, VA 22903',
        'clark': '291 McCormick Rd, Charlottesville, VA 22903',
        'aldy': '160 McCormick Rd, Charlottesville, VA 22904',
        'music': 'Cabell Dr L001, Charlottesville, VA 22904',
        'rice': '5 Engineer\'s Way, Charlottesville, VA 22903',
    }
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    student_location = locations.get(loc)
    tutor_location = locations2.get(other)
    print(tutor_location)
    if tutor_location == None:
        tutor_location = locations2.get('rice')
    now = datetime.now()
    #print(student_location, tutor_location)
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
        'name' : student_name,
        'phone' : student_phone
    }
    return render(request, 'tutorrequests/requests_detail.html', context)