import asyncio
import requests
from urllib3 import *
from working_with_files import Work_with_files

async def get_json_data():
	while(True):
		try:
			get_api=Work_with_files.get_api_keys()
			APIK_news=get_api['news_api']
			URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+APIK_news
			News_request=requests.get(URLnews)
			News=News_request.json()
			Work_with_files.save_news_data(News)


			City = "Novo mesto"
			Country = "SI"
			get_api_news=Work_with_files.get_api_keys()
			APIK_weather=get_api_news['weather_api']
			URL_main = "https://api.openweathermap.org/data/2.5/weather?q="+City+","+Country+"&appid="+APIK_weather+"&units=metric"
			URL_hours = "https://api.openweathermap.org/data/2.5/forecast?q="+City+"","+Country+"&appid="+APIK_weather+"&units=metric"
			r = requests.get(URL_main)
			read_weather = r.json()
			Work_with_files.save_weather_data_main(read_weather)
			r_hours = requests.get(URL_hours)
			read_weather_h=r_hours.json()
			Work_with_files.save_weather_data(read_weather_h)
			await asyncio.sleep(3600)
		except Exception as e:
			print(e)

loop=asyncio.get_event_loop()
loop.run_forever(get_json_data())
loop.close()