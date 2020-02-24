from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PhoneForm

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

                messages.success(request, f'Registered phone number successfully!')
                return redirect('home')
        else:
            form = PhoneForm()
        return render(request, 'register/reg_form.html', {'form': form})


