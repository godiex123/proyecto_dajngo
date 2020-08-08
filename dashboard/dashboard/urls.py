"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from apps.ControlInventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('buttons/',views.buttons,name='buttons'),
    path('cards/',views.cards,name='cards'),
    path('color/',views.color,name='color'),
    path('border/',views.border,name='border'),
    path('animation/',views.animation,name='animation'),
    path('other/',views.other,name='other'),
    path('password/',views.password,name='password'),
    path('error404/',views.error404,name='error404'),
    path('blank/',views.blank,name='blank'),
    path('charts/',views.charts,name='charts'),
    path('tables/',views.tables,name='tables'),
    path('utilities_color/',views.utilities_color,name='utilities_color'),
    path('utilities_border/',views.utilities_border,name='utilities_border'),
    path('utilities_animation/',views.utilities_animation,name='utilities_animation'),
    path('utilities_other/',views.utilities_other,name='utilities_other'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    
]