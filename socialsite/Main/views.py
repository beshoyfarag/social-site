from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
def index (request):
	return render(request,'main/Index.html')
def feed (request):
	return render(request,'main/feeds.html')
def friends (request):
	return render(request,'main/friends.html')
def profile (request):
	return render(request,'main/profile.html')
def goodie (request):
	return render(request,'main/goodie.html')
def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)

            login(request, user)

            return redirect('/Index/')

    else:

        form = UserCreationForm()

    return render(request, 'main/signup.html', {'form': form})
# Create your views here.
