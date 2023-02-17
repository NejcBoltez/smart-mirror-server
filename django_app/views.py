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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
import time

video = 'null'
usedCam = 'null'
class VideoCamera(object):
    def __init__(self):
        try:
            self.video = cv2.VideoCapture(0)
            (self.grabbed, self.frame) = self.video.read()
            c = threading.Thread(target=self.update, args=())
            c.setName("CAM_thread")
            c.start()
        except:
            self.video = cv2.VideoCapture(-1)
            (self.grabbed, self.frame) = self.video.read()
            c = threading.Thread(target=self.update, args=())
            c.setName("CAM_thread")
            c.start()
            
    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        #(self.grabbed, self.frame) = self.video.read()
        while True:
            (self.grabbed, self.frame) = self.video.read()
            time.sleep(0.1)
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def detect(camera):
    while True:
    
        _, img = gen(camera)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

def homePage(request):
    closeCamera()
    return render(request,'smartmirror_django/home.html')

def NewsPage(request):
    closeCamera()
    return render(request,'smartmirror_django/news.html')

def WeatherPage(request):
    closeCamera()
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
    closeCamera()
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
    closeCamera()
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

@gzip_page
def UserPicture(request):
    global usedCam
    try:
        if (usedCam == 'null'):
            usedCam = VideoCamera()
            return StreamingHttpResponse(gen(usedCam), content_type="multipart/x-mixed-replace;boundary=frame")
        else:
            return StreamingHttpResponse(gen(usedCam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:  # This is bad! replace it with proper handling
        print(e)

def closeCamera():
    global usedCam
    if (usedCam != 'null'):
        usedCam.__del__()
        usedCam = 'null'

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
def showCamera(request):
    return render(request,'smartmirror_django/cameraTest.html')

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        if image_data:
            # Decode the base64 image data
            image_data = base64.b64decode(image_data.split(',')[1])
            
            # Save the image to a file
            image_name = 'captured_image.png'
            with open(os.path.join('', image_name), 'wb') as f:
                f.write(image_data)
                
            # Return a JSON response indicating success
            return JsonResponse({'success': True})
        
    # Return a JSON response indicating failure
    return JsonResponse({'success': False})