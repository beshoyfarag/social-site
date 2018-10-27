from django.views.generic import ListView , DetailView
from django.conf.urls import url 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from Main import views as main_views
from feeds.models import Post


urlpatterns = [
   
    url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by("-date")[:25],
         template_name = "feeds/feeds.html")),
   
   url(r'^feed/', ListView.as_view(queryset = Post.objects.all().order_by("-date")[:25],
         template_name = "feeds/feeds.html")),
    
   url( r'^$', main_views.index, name='home'),
   url( r'^Index', main_views.index, name='Index'),
   url( r'^home', main_views.index, name='home'),
   url( r'^friends', main_views.friends, name='friends'),
   url( r'^profile', main_views.profile, name='profile'),
   url( r'^goodie', main_views.goodie, name='goodie'),
   url(r'^signup', main_views.signup, name='signup'),
   url(r'^login/$',auth_views.LoginView.as_view(template_name='main/login.html')) ,
   url(r'^feed/', ListView.as_view(queryset = Post.objects.all().order_by("-date")[:25],
         template_name = "feeds/feeds.html")),
    
   url(r'^(?P<slug>[-\w]+)$',DetailView.as_view (model = Post, template_name = 'feeds/post.html')),
    
    
   
  
   
]
