from django.urls import path
from geodjango import views

urlpatterns = [
   path('', views.index, name='index')
]