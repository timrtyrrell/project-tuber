from django.urls import path
from request_help import views

urlpatterns = [
    path('', views.request_help, name='request_help'),
    path('received', views.request_received, name='sending_help')
]