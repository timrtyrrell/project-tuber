from django.urls import path
from request_help import views

urlpatterns = [
    path('', views.HelpRequestView.as_view(), name='request_help'),
    path('received', views.request_received, name='sending_help'),
]