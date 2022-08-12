from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import User, Weather
from .forms import WeatherForm,UserForm
import uuid


def homePage(request):
    return render(request,'smartmirror_django/home.html')

def NewsPage(request):
    return render(request,'smartmirror_django/news.html')
    
def LoginPage(request):
    return render(request,'login.html')

def WeatherPage(request):
    if request.method == 'POST':

        form=WeatherForm(request.POST)
        Weather.objects.create(
            city = request.POST.get('city'),
            country = request.POST.get('country'),
            coordX = request.POST.get('coordX'),
            coordY = request.POST.get('coordY')
        )
    else:
        form=WeatherForm()
    context = {'form': form}
    return render(request,'smartmirror_django/weather.html', context)
def WeatherConfSave(request):
    weatherForm=WeatherForm()
    if request.method == 'POST':
        Weather.objects.create(
            city = request.POST.get('city'),
            country = request.POST.get('country'),
            coordX = request.POST.get('coordX'),
            coordY = request.POST.get('coordY')
        )
        print(request.POST.get('weather_api'))
    return redirect('home', RequestContext(request))

def NewUserPage(request):
    if request.method == 'POST':

        form=UserForm(request.POST)
        User.objects.create(
            name = request.POST.get('name'),
            #user_id = uuid.any(),
            #request.POST.get('user_id'),
            weather_api = request.POST.get('weather_api'),
            news_api = request.POST.get('news_api')
        )
    else:
        form=UserForm()
    
    context = {'form': form}
    return render(request,'smartmirror_django/user_prop.html', context)

def UserPage(request):
    if request.method == 'POST':

        form=UserForm(request.POST)
        User.objects.create(
            name = request.POST.get('name'),
            #user_id = uuid.any(),
            #request.POST.get('user_id'),
            weather_api = request.POST.get('weather_api'),
            news_api = request.POST.get('news_api')
        )
    else:
        form=UserForm()
    
    context = {'form': form}
    return render(request,'smartmirror_django/user_prop.html', context)