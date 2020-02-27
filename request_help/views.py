from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import HelpRequest

# Request Help
def request_help(request):
    if request.method == 'GET': 
        return render(request, 'request_help/request.html', {})
    if request.method == 'POST':
        help_request = HelpRequest.objects.create(class_name=request.POST['class_name'], topic_text=request.POST['topic_text'], location=request.POST['location'])
    return HttpResponseRedirect(reverse('sending_help'))

# Help request received
def request_received(request):
    return render(request, 'request_help/sendinghelp.html')