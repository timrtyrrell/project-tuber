from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from register.models import UserProfile
from django.contrib import messages


# Create your views here.

from .forms import StatusForm

def set_status(request):
    if not hasattr(request.user, 'userprofile'):
        return redirect('register')
    else:
        profile = request.user.userprofile
    current_status = ""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StatusForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            status = form.cleaned_data['status']
            location = form.cleaned_data['location']
            status_string = "yo"
            if status == "Yes":
                status = True
                status_string = "Available"
            else:
                status = False
                status_string = "Not available"

            profile.status = status
            profile.tutor_location = location
            profile.status_string = status_string
            
            profile.save()
            messages.success(request, f'Status updated!')
            return HttpResponseRedirect('/tutorStatus/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StatusForm() 
    
    return render(request, 'tutorStatus/set_status.html', {'form': form, 'current_status': profile.status_string})