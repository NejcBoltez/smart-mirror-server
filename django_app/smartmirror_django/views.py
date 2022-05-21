from django.shortcuts import redirect, render

def homePage(request):
    return render(request,'smartmirror_django/home.html')

def NewsPage(request):
    return render(request,'smartmirror_django/news.html')

def WeatherPage(request):
    return render(request,'smartmirror_django/weather.html')

def UserPage(request):
    return render(request,'smartmirror_django/user_prop.html')