from django.shortcuts import render
def index (request):
	return render(request,'main/Index.html')
def feed (request):
	return render(request,'main/feeds.html')
def friends (request):
	return render(request,'main/friends.html')
def profile (request):
	return render(request,'main/profile.html')
# Create your views here.
