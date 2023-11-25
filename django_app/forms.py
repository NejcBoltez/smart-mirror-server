from dataclasses import field
from .models import Weather, News, User
from django import forms

class UserForm(forms.Form):
    userName = forms.CharField(max_length=200)
    userPassword = forms.CharField(max_length=200)
    class Meta:
        model=User
        fields = '__all__'
class WeatherForm(forms.Form):
    weather_api = forms.CharField(max_length=200)
    weather_city = forms.CharField(max_length=200)
    weather_country = forms.CharField(max_length=200)
    weather_longitude = forms.CharField(max_length=200)
    weather_latitude = forms.CharField(max_length=200)
    use_coordinates = forms.BooleanField()
    class Meta:
        model=Weather
        fields = '__all__'

class NewsForm():
    news_api = forms.CharField(max_length=200)
    news_providers = forms.CharField(max_length=200)
    class Meta:
        model=News
        fields = '__all__'
