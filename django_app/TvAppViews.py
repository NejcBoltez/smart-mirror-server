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


def homePage(request,test):
	return render(request,'smartmirror_django/Tvapp/home.html',context)