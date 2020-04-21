from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import TutorProfile
from .forms import PhoneForm, TutorProfileForm

def register(request):
    if hasattr(request.user, 'userprofile'):
        return redirect('home')
    else:
        if request.method == 'POST':
            form = PhoneForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()

                name = profile.name
                messages.success(request, f'Registered {name} successfully!')
                return redirect('home')
        else:
            form = PhoneForm()
        return render(request, 'register/reg_form.html', {'form': form})


def editprofile(request):
    if not hasattr(request.user, 'userprofile'):
        return redirect('register')
    else:
        profile = request.user.userprofile

        if request.method == 'POST':
            form = PhoneForm(request.POST)
            if form.is_valid:
                data = request.POST.copy()
                profile.name = data.get('name')
                profile.phone = data.get('phone')
                profile.save()
                messages.success(request, f'Your profile was edited successfully!')       
        print(messages)        
        profile = request.user.userprofile
        form = PhoneForm({'name':profile.name, 'phone':profile.phone})
        return render(request, 'register/editprofile.html', {'form': form, 'profile':profile})


def becomeTutor(request):
    tutorProfile_list = TutorProfile.objects.order_by('id')
    form = TutorProfileForm()
    context = {'tutorProfile_list' : tutorProfile_list, 'form': form}
    return render(request, 'register/become_tutor.html', context)

@require_POST
def addClass(request): 
    form = TutorProfileForm(request.POST)

    if form.is_valid():
        class_name = TutorProfile(class_name = request.POST['class_name'])
        user = request.user.userprofile
        AddClass = TutorProfile(class_name=class_name, user=user)
        AddClass.save()
    return redirect('become_tutor')

def deleteClass(request, id): 
    item_to_delete = TutorProfile.objects.get(id=id)
    item_to_delete.delete()
    return redirect('become_tutor')