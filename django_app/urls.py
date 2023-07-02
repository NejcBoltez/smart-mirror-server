
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),
    path('news', views.NewsPage, name="news"),
    path('weather', views.WeatherPage, name="weather"),
    path('user_profile', views.UserPage, name="user_prop"),
    path('newUser/', views.NewUserPage, name="NewUserPage"),
    path('login', views.Login, name="LoginPage"),
    path('logout', views.Logout, name="LogoutPage"),
    path('process_image/', views.process_image, name='process_image'),
]
