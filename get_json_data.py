from urllib import request
from working_with_files import Work_with_files
import time
import json

while(True):
	try:
		get_api=Work_with_files.get_api_keys()
		APIK_news=get_api["news_api"]
		URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+APIK_news
		with request.urlopen(URLnews) as news_resp:
			news_response=json.loads(news_resp.read().decode())
		#print(news_response["articles"])

		Work_with_files.save_news_data(news_response)

		City = "Novo%20mesto"
		Country = "SI"
		get_api_news=Work_with_files.get_api_keys()
		APIK_weather=get_api_news["weather_api"]
		URL_main = "https://api.openweathermap.org/data/2.5/weather?q="+City+","+Country+"&appid="+APIK_weather+"&units=metric"
		URL_hours = "https://api.openweathermap.org/data/2.5/forecast?q="+City+","+Country+"&appid="+APIK_weather+"&units=metric"
		with request.urlopen(URL_main) as main_resp:
			read_weather=json.loads(main_resp.read().decode())
		
		Work_with_files.save_weather_data_main(read_weather)
		with request.urlopen(URL_hours) as hour_resp:
			read_weather_h=json.loads(hour_resp.read().decode())
		Work_with_files.save_weather_data(read_weather_h)
		time.sleep(3600)
		
	except Exception as e:
		print(e)
		time.sleep(3600)