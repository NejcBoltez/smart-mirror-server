from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Weather
from .forms import WeatherForm


def homePage(request):
    return render(request,'smartmirror_django/home.html')

def NewsPage(request):
    return render(request,'smartmirror_django/news.html')

def WeatherPage(request):
    if request.method == 'POST':

        form=WeatherForm(request.POST)
        Weather.objects.create(
            city = request.POST.get('City'),
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
    return redirect('home', RequestContext(request))
def UserPage(request):
    return render(request,'smartmirror_django/user_prop.html')