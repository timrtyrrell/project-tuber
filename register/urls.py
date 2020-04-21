from django.urls import path
from . import views

urlpatterns = [
    path('', views.becomeTutor, name='become_tutor'),
    path('add', views.addClass, name='add'),
]