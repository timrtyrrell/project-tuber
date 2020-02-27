from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import TutorStatus

# Create your views here.

def set_status(request):
    
    return render(request, 'tutorStatus/set_status.html')