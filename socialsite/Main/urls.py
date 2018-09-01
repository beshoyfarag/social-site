
from django.contrib import admin
from django.conf.urls import url 
from . import views 

urlpatterns = [
   url( r'^$', views.index, name='home'),
      url( r'^Index', views.index, name='Index'),
   url( r'^home', views.index, name='home'),
   url( r'^feed', views.feed, name='feed'),
   url( r'^friends', views.friends, name='friends'),
   url( r'^profile', views.profile, name='profile'),
    url( r'^goodie', views.goodie, name='goodie'),
   
]
