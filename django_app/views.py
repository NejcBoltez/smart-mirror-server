from django.shortcuts import redirect, render
from .models import Weather
from .forms import WeatherForm

def homePage(request):
    return render(request,'smartmirror_django/home.html')

def NewsPage(request):
    return render(request,'smartmirror_django/news.html')

def WeatherPage(request):

    form=WeatherForm()
    return render(request,'smartmirror_django/weather.html', {'form': form})
def WeatherConfSave(request):
    weatherForm=WeatherForm()
    if request.method == 'POST':
        Weather.objects.create(
            city = request.POST.get('name'),
            country = request.POST.get('name'),
            coordX = "",
            coordY = "",
            description=""
        )
def UserPage(request):
    return render(request,'smartmirror_django/user_prop.html')