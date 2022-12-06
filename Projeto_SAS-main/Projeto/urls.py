"""Projeto_SAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from app.models import models
from app.views import index, edit_profile
from app.views import Equipe
from django.urls import include, path

urlpatterns = [
    path('', index, name='index'),

    path('registro/', include('customauth.urls')), 
    path('edit_profile/<int:pk>/', edit_profile, name='url_edit_profile'),
   
    
]
