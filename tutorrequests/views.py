from django.shortcuts import render
from request_help.models import HelpRequest


def home(request):
    context = {
        'requests': HelpRequest.objects.all()
    }
    return render(request, 'tutorrequests/requests_home.html', context)

def details(request):
    return render(request, 'tutorrequests/requests_detail.html')