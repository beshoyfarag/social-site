
from django.contrib import admin
from django.conf.urls import url 
from . import views 

urlpatterns = [
   url( r'^$', views.index, name='home'),
   url( r'^home', views.index, name='home'),
   url( r'^feed', views.feed, name='feed'),
   url( r'^friends', views.friends, name='friends'),
   url( r'^profile', views.profile, name='profile'),
   
]
