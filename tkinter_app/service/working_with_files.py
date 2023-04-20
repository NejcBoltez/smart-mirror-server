import sys
sys.path.append('../controller')
sys.path.append('../repository')
import os
import json

class Work_with_files:
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
		api_keys_dir=os.path.join(BASE_DIR, "json_data"+os.path.sep+"api_keys.json")
		with open(api_keys_dir, "r") as f_api:
			read_api=json.load(f_api)
		return read_api
	
	def save_youtube_data(yt_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"youtube_data.json")
		with open(file_to_open,"w") as f_w:
			json.dump(yt_data,f_w)
	
	def save_news_data(news_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"news_data.json")
		with open(file_to_open,"w") as f_w:
			json.dump(news_data,f_w)
	
	def save_weather_data(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"forecast_data.json")
		with open(file_to_open,"w") as f_w:
			json.dump(weather_data,f_w)
	
	def save_weather_data_main(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"forecast_main.json")
		with open(file_to_open,"w") as f_w:
			json.dump(weather_data,f_w)
	
	def save_weather_data_today(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"forecast_today.json")
		with open(file_to_open,"w") as f_w:
			json.dump(weather_data,f_w)
	
	def read_news_data():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"news_data.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		return r_p
	
	def read_weather_data():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"forecast_data.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		return r_p
	
	def read_weather_main():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"forecast_main.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		return r_p
	
	def read_weather_today():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		file_to_open=os.path.join(BASE_DIR, "json_data"+os.path.sep+"forecast_today.json")
		with open(file_to_open,"r") as f_r:
			r_p=json.load(f_r)
		return r_p