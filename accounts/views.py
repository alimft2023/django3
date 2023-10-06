from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def addeducation(request):
    return render(request,'accounts/add-education.html',{})

def addexperience(request):
    return render(request,'accounts/add-experience.html',{})

def createprofile(request):
    return render(request,'accounts/create-profile.html',{})

def dashboard(request):
    return render(request,'accounts/dashboard.html',{})

def login(request):
    return render(request,'accounts/login.html',{})

def profile(request):
    userprofile=UserProfile.objects.get(id=2)
    return render(request,'accounts/profile.html',{"userprofile":userprofile})

def profiles(request):
    return render(request,'accounts/profiles.html',{})

def register(request):
    return render(request,'accounts/register.html',{})