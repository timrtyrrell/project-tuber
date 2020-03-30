from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import HelpRequest
from .forms import HelpRequestForm

from django.views.generic.edit import CreateView


# Request Help
class HelpRequestView(CreateView):
    model = HelpRequest
    form_class = HelpRequestForm
    template_name = 'request_help/request.html'
    success_url = 'received'

# Help request received
def request_received(request):
    return render(request, 'request_help/sendinghelp.html')