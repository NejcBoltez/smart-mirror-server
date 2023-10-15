from django.shortcuts import render
from .working_with_files import Work_with_files

def homePage(request):
	context = { 'data': '', 'values':''}
	context['weatherData'] = Work_with_files.read_weather_main()
	return render(request,'smartmirror_django/Dashboard/home.html', context)