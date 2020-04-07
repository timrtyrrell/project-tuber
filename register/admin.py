from django.contrib import admin
from .models import UserProfile, TutorProfile

admin.site.register(UserProfile)
admin.site.register(TutorProfile)