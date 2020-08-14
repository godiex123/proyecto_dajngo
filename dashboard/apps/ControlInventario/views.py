from django.shortcuts import render
from apps.ControlInventario.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'landing/base/index.html',{})






@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.username = user.email.split('@')[0]
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'Dashboard/base/register.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'Dashboard/base/login.html', {})

















def dashboard(request):
    return render(request,'Dashboard/base/index.html',{})
'''
def login(request):
    return render(request,'Dashboard/base/login.html',{})

def register(request):
    return render(request,'Dashboard/base/register.html',{})
'''
def buttons(request):
    return render(request,'Dashboard/base/buttons.html',{})

def cards(request):
    return render(request,'Dashboard/base/cards.html',{})

def color(request):
    return render(request,'Dashboard/base/color.html',{})

def border(request):
    return render(request,'Dashboard/base/border.html',{})

def animation(request):
    return render(request,'Dashboard/base/animation.html',{})

def other(request):
    return render(request,'Dashboard/base/other.html',{})

def password(request):
    return render(request,'Dashboard/base/password.html',{})

def error404(request):
    return render(request,'Dashboard/base/error404.html',{})

def blank(request):
    return render(request,'Dashboard/base/blank.html',{})

def charts(request):
    return render(request,'Dashboard/base/charts.html',{})

def tables(request):
    return render(request,'Dashboard/base/tables.html',{})

def utilities_color(request):
    return render(request,'Dashboard/base/utilities-color.html',{})
    
def utilities_border(request):
    return render(request,'Dashboard/base/utilities-border.html',{})

def utilities_animation(request):
    return render(request,'Dashboard/base/utilities-animation.html',{})

def utilities_other(request):
    return render(request,'Dashboard/base/utilities-other.html',{})

def forgot_password(request):
    return render(request,'Dashboard/base/forgot_password.html',{})



