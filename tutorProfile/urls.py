from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tutor_profile'),
    path('add', views.addClass, name='add')
]