
from django.contrib import admin
from django.urls import path, include
from . import UserUIViews
from . import SmartMirrorViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserUIViews.homePage, name="home"),
    path('news', UserUIViews.NewsPage, name="news"),
    path('weather', UserUIViews.WeatherPage, name="weather"),
    path('user_profile', UserUIViews.UserPage, name="user_prop"),
    path('newUser/', UserUIViews.NewUserPage, name="NewUserPage"),
    path('login', UserUIViews.Login, name="LoginPage"),
    path('logout', UserUIViews.Logout, name="LogoutPage"),
    path('process_image/', UserUIViews.process_image, name='process_image'),
    path('smart_mirror/<str:test>', SmartMirrorViews.homePage, name='process_image')
]
