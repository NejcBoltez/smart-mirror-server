from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.template import RequestContext
from .models import User, Weather
from .forms import WeatherForm,UserForm
import uuid
import threading
import cv2
from django.views.decorators.gzip import gzip_page
import time

video = 'null'
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
            time.sleep(0.5)
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def homePage(request):
    return render(request,'smartmirror_django/home.html')

def NewsPage(request):
    return render(request,'smartmirror_django/news.html')

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

class Set_cam():
    def main(self):
        self.used_cam=''
        UserPicture()

@gzip_page
def UserPicture(request):
    #print(video)
    try:
        cam_thread=threading.enumerate()
        for c in cam_thread:
            print(c)
            print(c.getName())
            if(c.getName() == 'CAM_thread'):
                c.join()
        try:
            cam_thread=threading.enumerate
            for c in cam_thread:
                print(c)
        except Exception as e:
            cam_thread=''
        print(threading.current_thread())
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:  # This is bad! replace it with proper handling
        print(e)

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