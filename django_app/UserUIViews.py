from django.shortcuts import redirect, render
from django.http import StreamingHttpResponse, JsonResponse
from django.template import RequestContext
from .models import Weather, News
from .forms import WeatherForm,UserForm
import uuid
import cv2
import os
import base64
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
import json
import base64
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


loginedUser = 'Nejc'
newsData = []

newsProviders = ["Google","24ur","rtvslo","siol","racunalniske novice"]

#Return the Home page
def homePage(request):
	return render(request,'smartmirror_django/webUI/home.html')

#remove the news provider from the json
def removeNewsCode(request):
	data = getDataFromJSON()
	id = 1
	print("ID" + id)
	providers = ["Google","24ur","rtvslo","siol","racunalniske novice"]
	newsData = data['newsData'].pop(id)
	context = { 'data': newsData,'providers':providers}
	return render(request,'smartmirror_django/webUI/news.html',context)

#Return the News page
@csrf_exempt
def NewsPage(request):

	global newsData
	global newsProviders

	if request.method == 'POST':
		News.objects.create(
			user_id = request.user.id,
			news_api = request.POST.get('news_api'),
			news_file = request.user.name + '/news.json',
		)
		saveNewsCodesJSON(str(request.body.decode().replace("news=","").replace("+", " ")).split('&'))
	
	if request.method == 'GET':
		print (request.META['QUERY_STRING'])
		try :
			if ('add' in request.META['QUERY_STRING']):
				print(request.GET.get('add'))
				newsData.append("")
				print(newsData)
			elif ('remove' in request.META['QUERY_STRING']):
				print(request.GET.get('remove'))
				newsData.pop(int(request.GET.get('remove')))
			else:
				data = getDataFromJSON()
				newsData = data['newsData']
		except Exception as e:
			data = getDataFromJSON()
			newsData = data['newsData']
	print(newsData)
	context = { 'data': newsData,'providers':newsProviders}
	return render(request,'smartmirror_django/webUI/news.html',context)

#Return the Weather Page
def WeatherPage(request):
	if request.method == 'POST':
		print("TEST")
		print (request.body.decode())
		print (request.POST.get('api_key'))
		Weather.objects.create(
			user_id = request.user.id,
			weather_api = request.POST.get('weather_api'),
			weather_city = request.POST.get('weather_city'),
			weather_country = request.POST.get('weather_country'),
			weather_longitude = request.POST.get('weather_longitude'),
			weather_latitude = request.POST.get('weather_latitude'),
			weather_file = request.user.name + '/weather.json',
		)
		#saveWeatherDataToJSON(request.body.decode().split("&"))
	else:
		form=WeatherForm()
	form = WeatherForm()
	context = {'form': form}
	return render(request,'smartmirror_django/webUI/weather.html', context)


#Return the page to create a new user
def NewUserPage(request):
	if request.method == 'POST':

		form=UserCreationForm(request.POST)
		User.objects.create(
			username = request.POST.get('username'),
			password = request.POST.get('password1')
		)
		'''BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, "../Users")
		user_dir=str(image_dir)+"/"+str(request.POST.get('userName'))
		os.mkdir(user_dir)
		os.chmod(user_dir, 0o777)
		file_to_open=os.path.join(BASE_DIR, "../Users" + os.path.sep + "users.json")
		userData = "" 
		with open(file_to_open,"r") as f_w:
			userData = json.load(f_w)
		
		userData['userID']=str(uuid.uuid4())
		userData['user']=request.POST.get('userName')
		userData['encryptedPassword'] = str(base64.b64encode(request.POST.get('userPassword').encode('ascii')))
		userData['apiKeys']['weather_api_key'] = request.POST.get('weather_api')
		userData['apiKeys']['news_api_key'] = request.POST.get('news_api')
		print(userData)

		with open(user_dir + os.path.sep + request.POST.get('userName') + ".json","w") as f_w:
			json.dump(userData,f_w)'''
	else:
		form=UserCreationForm()
	
	context = {'form': form}
	return render(request,'smartmirror_django/webUI/create_new_user.html', context)

#Return the user properties page
def UserPage(request):
	if request.method == 'POST':

		form=UserCreationForm(request.POST)
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../Users"+os.path.sep+"users.json")
		userData = "" 
		with open(file_to_open,"r") as f_w:
			userData = json.load(f_w)
		userData['user']=request.POST.get('userName')
		userData['encryptedPassword'] = str(base64.b64encode(request.POST.get('userPassword').encode('ascii'))),
		userData['apiKeys']['weather_api_key'] = request.POST.get('weather_api'),
		userData['apiKeys']['news_api_key'] = request.POST.get('news_api')
		print(userData)

		with open(file_to_open,"w") as f_w:
			json.dump(userData,f_w)
		
	else:
		form=UserCreationForm()
	
	context = {'form': form}
	return render(request,'smartmirror_django/webUI/user_prop.html', context)

#Save the user image for face recognition
@csrf_exempt
def process_image(request):
	if request.method == 'POST':
		image_data = request.POST.get('image')
		if image_data:
			# Decode the base64 image data
			image_data = base64.b64decode(image_data.split(',')[1])

			im_arr = np.frombuffer(image_data, dtype=np.uint8)  # im_arr is one-dim Numpy array
			img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
			face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			faces = face_cascade.detectMultiScale(gray, 1.1, 4)
			for (x, y, w, h) in faces:
				cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
				face = gray[y:y + h, x:x + w]
			# Save the image to a file
			image_name = './Users/Nejc/captured_image.png'
			cv2.imwrite(image_name, face)
				
			# Return a JSON response indicating success
			return JsonResponse({'success': True})
		
	# Return a JSON response indicating failure
	return JsonResponse({'success': False})

#Getting data from JSON file
def getDataFromJSON():
	data = ""
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	file_to_open=os.path.join(BASE_DIR, "../Users"+os.path.sep+loginedUser+os.path.sep+loginedUser+".json")
	userData = "" 
	with open(file_to_open,"r") as f_w:
		data = f_w.read()
	return json.loads(data)

#Saving data to JSON
def saveDataToJSON():
	data = ""
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	file_to_open=os.path.join(BASE_DIR, "../Users"+os.path.sep+loginedUser+os.path.sep+loginedUser+".json")
	userData = "" 
	with open(file_to_open,"r") as f_w:
		data = f_w.read()
	return json.loads(data)

#Saving News providers to JSON
def saveNewsCodesJSON(newsCodes):
	data = ""
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	file_to_open=os.path.join(BASE_DIR, "../Users"+os.path.sep+loginedUser+os.path.sep+"nejc.json")
	userData = "" 
	with open(file_to_open,"r") as f_w:
		data = json.load(f_w)
	data["newsData"] = newsCodes
	with open(file_to_open,"w") as f_w:
		json.dump(data,f_w)
	#return json.loads(data)

#Save weather data to JSON	
def saveWeatherDataToJSON(weatherData):
	print(weatherData)
	data = ""
	if ("csrf" in weatherData[0]):
		print(True)
		del weatherData[0]
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	file_to_open=os.path.join(BASE_DIR, "../Users"+os.path.sep+loginedUser+os.path.sep+"nejc.json")
	userData = "" 
	with open(file_to_open,"r") as f_w:
		data = json.load(f_w)
	data["weatherData"] = weatherData
	with open(file_to_open,"w") as f_w:
		json.dump(data,f_w)

#Login function
@csrf_exempt
def Login(request):
	if request.method == 'POST':
		user = authenticate(username="nejc", password="Gabrje157")
		if user is not None:
			print(user)
			login(request, user)
			return render(request,'smartmirror_django/webUI/home.html')
		else:
			print("Problem")
	else:
		return render(request,'smartmirror_django/webUI/login.html')
	
#Logout function
@csrf_exempt
def Logout(request):
	logout(request)
	return render(request,'smartmirror_django/webUI/login.html')