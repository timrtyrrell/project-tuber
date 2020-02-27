from django.urls import path
from tutorStatus import views

urlpatterns = [
    path('', views.set_status, name='tutor_status')
]