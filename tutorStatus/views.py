from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from register.models import UserProfile
from django.contrib import messages


# Create your views here.

def set_status(request):

    if not hasattr(request.user, 'userprofile'):
        return redirect('register')
    else:
        profile = request.user.userprofile

    tutor_status = CharField(request.POST)
    bool_status = False
    if tutor_status == "Yes":
        bool_status = True
    else:
        bool_status = False        
    
    profile.status = bool_status

    profile.save()

    messages.success(request, f'Status updated!')

    return render(request, 'tutorStatus/set_status.html')