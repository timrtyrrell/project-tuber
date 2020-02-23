from django.shortcuts import render

def request_help(request):
    return render(request, 'request_help/request.html', {})