from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewList

def register(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            c = form.cleaned_data["course"]
            t = ToDoList(name=n)
            t.save()
    else:
        form = CreateNewList()
    return render(response, 'tutorProfile/register.html', {"form":form})


