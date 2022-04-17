#import requests
from urllib import request
from working_with_files import Work_with_files
import time
import json

#def get_json_data():
while(True):
	try:
		get_api=Work_with_files.get_api_keys()
		APIK_news=get_api['news_api']
		URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+APIK_news
		#News_send=request.Request(URLnews)
		#News_request=request.urlopen(URLnews).read()#request.Request(URLnews)
		#print(type(str(News_request)))
		with request.urlopen(URLnews) as news_resp:
			news_response=json.loads(news_resp.read().decode())
			print(news_response["articles"])
			print("TEST")
		#News=json.loads(News_request.decode('ISO-8859-1'))#news_response.json()
		Work_with_files.save_news_data(news_response)

		City = "Novo%20mesto"
		Country = "SI"
		get_api_news=Work_with_files.get_api_keys()
		APIK_weather=get_api_news['weather_api']
		URL_main = "https://api.openweathermap.org/data/2.5/weather?q="+City+","+Country+"&appid="+APIK_weather+"&units=metric"
		URL_hours = "https://api.openweathermap.org/data/2.5/forecast?q="+City+","+Country+"&appid="+APIK_weather+"&units=metric"
		#r = request.Request(URL_main)
		with request.urlopen(URL_main) as main_resp:
			read_weather=json.loads(main_resp.read().decode())
			print("TEST")
			print(read_weather)
		
		Work_with_files.save_weather_data_main(read_weather)
		with request.urlopen(URL_hours) as hour_resp:
			read_weather_h=json.loads(hour_resp.read().decode())
			print("TEST")
			print(read_weather_h)
		#read_weather = r.json()
		#Work_with_files.save_weather_data_main(read_weather)
		#r_hours = request.Request(URL_hours)
		#read_weather_h=r_hours.json()
		Work_with_files.save_weather_data(read_weather_h)
		time.sleep(3600)
		
	except Exception as e:
		print(e)
		time.sleep(3600)

#loop=asyncio.get_event_loop()
#loop.run_forever(get_json_data())
#loop.close()