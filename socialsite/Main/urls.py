
from django.conf.urls import url 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
   
   url( r'^$', views.index, name='home'),
   url( r'^Index', views.index, name='Index'),
   url( r'^home', views.index, name='home'),
   url( r'^friends', views.friends, name='friends'),
   url( r'^profile', views.profile, name='profile'),
   url( r'^goodie', views.goodie, name='goodie'),
   url(r'^signup', views.signup, name='signup'),
   url(r'^login/',auth_views.LoginView.as_view(template_name='main/login.html')) ,
   


   

]