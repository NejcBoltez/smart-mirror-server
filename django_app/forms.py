from dataclasses import field
from .models import Weather

class WeatherForm():
    class Meta:
        model=Weather
        fields = '__all__'