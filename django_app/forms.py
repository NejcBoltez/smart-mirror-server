from dataclasses import field
from .models import Weather, News, UserData
from django import forms

class UserDataForm(forms.Form):
    weather_api = forms.CharField(max_length=200)
    news_api = forms.CharField(max_length=200)
    class Meta:
        model=UserData
        fields = '__all__'
        
class WeatherForm(forms.Form):
    weather_api = forms.CharField(max_length=200)
    weather_city = forms.CharField(max_length=200)
    weather_country = forms.CharField(max_length=200)
    weather_longitude = forms.CharField(max_length=200)
    weather_latitude = forms.CharField(max_length=200)
    class Meta:
        model=Weather
        fields = '__all__'

class NewsForm():
    news_api = forms.CharField(max_length=200)
    news_providers = forms.CharField(max_length=200)
    class Meta:
        model=News
        fields = '__all__'
