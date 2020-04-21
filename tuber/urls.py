"""tuber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from loginGoogle import views as core_views
from register import views as register_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', auth_views.LoginView.as_view(), name='logout'),
    url(r'^request/', include('request_help.urls')),
    url(r'^tutorStatus/', include('tutorStatus.urls')),
    path('register/', register_views.register, name="register"),
    path('editprofile/', register_views.editprofile, name='editprofile'),
    path('tutorrequests/', include('tutorrequests.urls'), name='tutorrequests'),
    path('becometutor/', include('register.urls')),
    path('delete/<int:id>', register_views.deleteClass, name='delete')
]
