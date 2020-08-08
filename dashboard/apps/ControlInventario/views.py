from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'landing/base/index.html',{})

def dashboard(request):
    return render(request,'Dashboard/base/index.html',{})

def login(request):
    return render(request,'Dashboard/base/login.html',{})

def register(request):
    return render(request,'Dashboard/base/register.html',{})

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



