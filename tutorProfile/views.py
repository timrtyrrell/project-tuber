from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import TutorProfile
from .forms import TutorProfileForm

def index(request):
    tutorProfile_list = TutorProfile.objects.order_by('id')
    form = TutorProfileForm()
    context = {'tutorProfile_list' : tutorProfile_list, 'form': form}
    return render(request, 'tutorProfile/register.html', context)

@require_POST
def addClass(request): 
    form = TutorProfileForm(request.POST)

    if form.is_valid():
        new_class = TutorProfile(class_name = request.POST['class_name'])
        new_class.save()

    return redirect('tutor_profile')
