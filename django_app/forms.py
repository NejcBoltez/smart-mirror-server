from dataclasses import field
from .models import Weather, News, User
from django import forms

class UserForm(forms.Form):
    
    #host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    userName = forms.CharField(max_length=200)
    userPassword = forms.CharField(widget=forms.PasswordInput)
    weather_api = forms.CharField(max_length=200)
    news_api = forms.CharField(max_length=200)
    class Meta:
        model=User
        fields = '__all__'
class WeatherForm(forms.Form):
    
    #host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    country = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    coordX = forms.CharField(max_length=200)
    coordY = forms.CharField(max_length=200)
    class Meta:
        model=Weather
        fields = '__all__'

class NewsForm():
    news_to_select = forms.CharField(max_length=200)
    class Meta:
        model=News
        fields = '__all__'
