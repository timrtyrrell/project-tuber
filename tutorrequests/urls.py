from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="requests-home"),
    path('details', views.details, name="requests-details"),
]