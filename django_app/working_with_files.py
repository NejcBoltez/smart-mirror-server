import sys
import os
import json
from youtube_search import YoutubeSearch
import subprocess
import sys
from urllib import request
from urllib import parse

class Work_with_files:
	def get_yt_data(search_for):
		results = YoutubeSearch(str(search_for).replace("_", " "), max_results=20).to_json()
		get_results=json.loads(results)
		#save_youtube_data(get_results)
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"youtube_data.json")
		with open(file_to_open,"w") as f_w:
			json.dump(get_results,f_w)
		#print(get_results)
		return get_results

	def getSaved_yt_data():
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"youtube_data.json")
		get_results=[]
		with open(file_to_open,"r") as f_r:
			get_results=json.load(f_r)
		return get_results

	def stream_youtube(videoToPlay):
		print("VIDEO INDEX: "+str(videoToPlay))
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"youtube_data.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		print(r_p['videos'][videoToPlay])
		r_p['videos'][videoToPlay]['videoURL'] = "https://www.youtube.com/embed/" + r_p['videos'][videoToPlay]['id'] + "?autoplay=1"
		return r_p['videos'][videoToPlay]
	def save_image(url_of_image):
		url_split=url_of_image.split(".")
		file_end=url_split[len(url_split)-1]
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		wiki=os.path.join(BASE_DIR, "./wiki_pictures/wiki.jpg")
		file_name="./wiki_pictures/wiki."+str(file_end)
		if(os.path.isfile(file_name)):
			os.remove(file_name)
		try:
			start_popup=subprocess.Popen(["wget", "-O",file_name, url_of_image])
			start_popup.wait()
		except Exception as e:
			print(e)
	def get_wiki_data(question):
		wiki_api_url="https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|pageimages&exsentences=6&pithumbsize=500&exintro&explaintext&redirects=1&titles="+str(question.replace("_", "%20"))#str(title[0])
		print(wiki_api_url)
		with request.urlopen(wiki_api_url) as wiki_resp:
			read_wiki=json.loads(wiki_resp.read().decode())
			#print(read_wiki)

		wiki_response=list(read_wiki["query"]["pages"].values())[0]
		title=wiki_response["title"]
		answer=wiki_response["extract"]
		#print(wiki_response["query"]["pages"].values())
		try:
			url_of_image=wiki_response["thumbnail"]["source"]
		except Exception as e:
			print(str(e))
			wiki_response["thumbnail"]={"source":""}
		print(wiki_response)
		#save_image(wiki_api_url)
		'''url_split=url_of_image.split(".")
		file_end=url_split[len(url_split)-1]
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		wiki=os.path.join(BASE_DIR, "./wiki_pictures/wiki.jpg")
		file_name="./wiki_pictures/wiki."+str(file_end)
		if(os.path.isfile(file_name)):
			os.remove(file_name)
		try:
			start_popup=subprocess.Popen(["wget", "-O",file_name, url_of_image])
			start_popup.wait()
		except Exception as e:
			print(e)'''
		return wiki_response
	def create_dir_for_user(new_user):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, "../Users")
		dir_path=str(image_dir)+"/"+str(new_user)
		os.mkdir(dir_path)
		os.chmod(dir_path, 0o777)
	
	def remove_file(file_path):
		os.remove(file_path)	    	
	
	def get_last_mod_file(path):
		files = os.listdir(path)
		paths = [os.path.join(path, basename) for basename in files]
		return min(paths, key=os.path.getctime)
	
	def get_api_keys():
		read_api=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		api_keys_dir=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"api_keys.json")
		with open(api_keys_dir, "r") as f_api:
			read_api=json.load(f_api)
		return read_api
	
	def save_youtube_data(yt_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"youtube_data.json")
		with open(file_to_open,"w") as f_w:
			json.dump(yt_data,f_w)
	
	def save_news_data(news_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"news_data.json")
		with open(file_to_open,"w") as f_w:
			json.dump(news_data,f_w)
	
	def save_weather_data(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"forecast_data.json")
		with open(file_to_open,"w") as f_w:
			json.dump(weather_data,f_w)
	
	def save_weather_data_main(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"forecast_main.json")
		with open(file_to_open,"w") as f_w:
			json.dump(weather_data,f_w)
	
	def save_weather_data_today(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"forecast_today.json")
		with open(file_to_open,"w") as f_w:
			json.dump(weather_data,f_w)
	
	def read_news_data():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"news_data.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		return r_p
	def get_all_dates_for_weather():
		r_p=""
		allDates = []
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"forecast_data.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		
		for i in r_p['list']:
			date = i['dt_txt'].split(" ")[0]
			if (date not in allDates):
    				allDates.append(date)
		return allDates
	def read_weather_data():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"forecast_data.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		
		for i in r_p['list']:
			i['date'] = i['dt_txt'].split(" ")[0]
			print(i)
		return r_p
	
	def read_weather_main():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"forecast_main.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		print(r_p)
		
		return r_p
	
	def read_weather_today():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "../json_data"+os.path.sep+"forecast_today.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		return r_p