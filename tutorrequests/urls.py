from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="requests-home"),
    path('details/<pk>', views.details, name="requests-details"),
    path('delete/<pk>', views.delete, name="delete"),
]