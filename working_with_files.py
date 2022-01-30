import os
import json

class Work_with_files:
	def save_start_phrases(phrases):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		start_phrases=os.path.join(BASE_DIR, 'start_phrases.json')	
		with open(start_phrases, "r") as f_r:
			f_read=f_r.read()
		read_phrases=f_read.replace(']','')
		new_phrases={
			"user" : "",
			"start_phrases" : '"'+str(phrases)+'"'
		}
		with open(start_phrases,"w") as f_w:
			f_w.write(str(read_phrases)+','+str(new_phrases).replace("'", '"')+"]")
		print(f_read)
	def create_dir_for_user(new_user):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, '../Users')
		dir_path=str(image_dir)+'/'+str(new_user)
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
		api_keys_dir=os.path.join(BASE_DIR, "../api_keys.json")
		with open(api_keys_dir, "r") as f_api:
			read_api=json.load(f_api)
		return read_api

	def print_process_to_file(p_id, p_name):
		p="{"
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "../open_processes.json")
		
		with open(open_processes, "r") as f_r:
			f_read=f_r.read()
			p=p+f_read.replace("{","").replace("}","")
			print("Read lines:"+str(p))

		p_to_file="'"+p_name+"': '"+p_id+"'}"
		p_to_file=p_to_file.replace("'",'"')
		if (p=="{"):
			p=p+p_to_file
		else:
			p=p+","+p_to_file
		print(p)
		with open(open_processes,"w") as f_w:
			f_w.write(str(p))

	def remove_process_from_file(p_id):
		p="{"
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "../open_processes.json")
		with open(open_processes, "r") as f_r:
			f_read=f_r.read()
			p=p+f_read.replace("{","").replace("}","")
		p_split=p.split(",")
		print(p_split)
		p_new="{"
		for s in p_split:
			if (p_id in s):
				continue
			else:
				if(p_new=="{"):
					p_new=p_new+s	
				else:
					p_new=p_new+","+s
		p_new=p_new+"}"
		with open(open_processes, "w") as f_w:
			f_w.write(p_new)

	def read_process_from_file():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "../open_processes.json")
		with open(open_processes, "r") as f_r:
			#f_read=f.read()
			r_p=json.load(f_r)
		return r_p

	def remove_all_processes_from_file():
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "../open_processes.json")
		with open(open_processes, "w") as f:
			f.write("")
		#return f_read
	def save_youtube_data(yt_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "youtube_data.json")
		with open(open_processes,"w") as f_w:
			json.dump(yt_data,f_w)
	def save_news_data(news_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "news_data.json")
		with open(open_processes,"w") as f_w:
			json.dump(news_data,f_w)
	def save_weather_data(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "forecast_data.json")
		with open(open_processes,"w") as f_w:
			json.dump(weather_data,f_w)
	def save_weather_data_main(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "forecast_main.json")
		with open(open_processes,"w") as f_w:
			json.dump(weather_data,f_w)
	def save_weather_data_today(weather_data):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "forecast_today.json")
		with open(open_processes,"w") as f_w:
			json.dump(weather_data,f_w)
	def read_news_data():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "news_data.json")
		with open(open_processes,"r") as f_r:
			r_p=json.load(f_r)
		#print(r_p)
		return r_p
	def read_weather_data():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "forecast_data.json")
		with open(open_processes,"r") as f_r:
			r_p=json.load(f_r)
		return r_p
	def read_weather_main():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "forecast_main.json")
		with open(open_processes,"r") as f_r:
			r_p=json.load(f_r)
		#print("TEST: "+str(r_p))
		return r_p
	def read_weather_today():
		r_p=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		open_processes=os.path.join(BASE_DIR, "forecast_today.json")
		with open(open_processes,"r") as f_r:
			r_p=json.load(f_r)
		return r_p