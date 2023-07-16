from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, StreamingHttpResponse, JsonResponse
from django.template import RequestContext
from .models import User, Weather
from .forms import WeatherForm,UserForm
import uuid
import threading
import cv2
import os
import base64
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
import time
import json
import base64
from django.contrib.auth import authenticate, login, logout
from .working_with_files import Work_with_files




loginedUser = 'Nejc'
youtubeData = []

newsProviders = ["Google","24ur","rtvslo","siol","racunalniske novice"]

def homePage(request,test):
	global youtubeData
	newsData = 1
	context = { 'data': newsData, 'values':youtubeData}
	if request.method == "GET":
		print(request.path)
		context['data'] = test
		if ("weather" in test):
			context['values'] = Work_with_files.get_yt_data("Iron Man")['videos']
		elif ("news" in test):
			context['values'] = Work_with_files.read_news_data()['articles']
		elif ("ytSearch" in test):
			context['values'] = Work_with_files.get_yt_data("Iron Man")['videos']
		elif ("ytStream" in test):
			context['values'] = Work_with_files.stream_youtube(0)
	providers = ["Google","24ur","rtvslo","siol","racunalniske novice"]
	return render(request,'smartmirror_django/SmartMirrorTemplate/home.html',context)