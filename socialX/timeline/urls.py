from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('main', views.timeline ,name='timeline'),
    path('profile', views.profile ,name='profile'),
]
