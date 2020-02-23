from django.shortcuts import render

from django.http import HttpResponse

from .models import HelpRequest

# Request Help
def request_help(request):
    if request.method == 'GET': 
        return render(request, 'request_help/request.html', {})
    elif request.method == 'POST':
        help_request = HelpRequest.objects.create(class_name=request.POST['class_name'], topic_text=request.POST['topic_text'])
    return HttpResponseRedirect(reverse('request_help:request'))