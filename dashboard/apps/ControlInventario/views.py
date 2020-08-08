from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'LandingPage/index.html',{})

def dashboard(request):
    return render(request,'Dashboard/index.html',{})
