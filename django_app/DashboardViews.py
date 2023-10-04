from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, StreamingHttpResponse, JsonResponse
from django.template import RequestContext
from .models import User, Weather
from .forms import WeatherForm,UserForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
import base64
from django.contrib.auth import authenticate, login, logout
from .working_with_files import Work_with_files

def homePage(request):
	context = { 'data': '', 'values':''}
	context['weatherData'] = Work_with_files.read_weather_main()
	return render(request,'smartmirror_django/Dashboard/home.html', context)