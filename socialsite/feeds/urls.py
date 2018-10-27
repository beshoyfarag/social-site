from django.views.generic import ListView , DetailView
from django.conf.urls import url 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from feeds.models import Post


urlpatterns = [
   
    url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by("-date")[:25],
         template_name = "feeds/feeds.html")),

    url(r'^(?P<slug>[-\w]+)$',DetailView.as_view (model = Post, template_name = 'feeds/post.html')),
  

  
   
]
