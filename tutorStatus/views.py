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

            if status == "Yes":
                status = True
            else:
                status = False

            profile.status = status
            profile.tutor_location = location
            
            profile.save()
            messages.success(request, f'Status updated!')
            return HttpResponseRedirect('/tutorStatus/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StatusForm()

    if profile.status == "False":
        current_status = "Not available"
    else:
        current_status = "Available"
    
    return render(request, 'tutorStatus/set_status.html', {'form': form, 'current_status': current_status})