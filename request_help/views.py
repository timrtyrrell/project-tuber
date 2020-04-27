from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import HelpRequest
from .forms import HelpRequestForm

from django.views.generic.edit import CreateView
from django.contrib.auth.models import User



# Request Help
class HelpRequestView(CreateView):
    model = HelpRequest
    form_class = HelpRequestForm
    template_name = 'request_help/request.html'
    success_url = 'received'
    def post(self, request, **kwargs):
        form = HelpRequestForm(request.POST)
        if form.is_valid():                
            post = form.save(commit = False)
            post.name = request.user.userprofile.name
            post.phone = request.user.userprofile.phone
            post.save()
            return render(request, 'request_help/sendinghelp.html')

# Help request received
def request_received(request):
    HelpRequest.user = request.user
    return render(request, 'request_help/sendinghelp.html')