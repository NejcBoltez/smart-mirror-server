import subprocess
import os
import signal
import Virtual_asistent as asistant
import multiprocessing
from working_with_files import Work_with_files
from speech_listen import Speaking
from news import display_news
from wikipedia_window import Wikipedia_show
from youtube import yt_search
from youtube_stream import Video
from weather import weather_GUI
from calibrate import Calibrate
import asyncio

		
class Do_for_command:
	def __call__(args):
			try: 
				print('test:     '+args)
			except:
				print('')
	async def main(self, command, user, displayed, tabcontrol):

		print('WE HAVE IT')
		print(type(tabcontrol))
		numbers_int=["1","2","3","4","5","6","7","8","9","10"]
		numbers_string=["one","two","three","four","five","six","seven","eight","nine","ten"]
		position=["first", "second","thirth","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
		await asyncio.sleep(1)
		

		show_news=displayed
		tabcontrol=tabcontrol
		command=command.lower()
		command_search=""
		if (" for " in command):
			command_search=command.split(" for ")[1]
		if (command!=""):
			if("forecast" in command or "weather" in command):
				if (command_search==""):
					command_search="today"
					forecast_task=asyncio.create_task(weather_GUI.main(self, command_search, tabcontrol))
					await forecast_task
					
				else:
					forecast_task=asyncio.create_task(weather_GUI.main(self, command_search, tabcontrol))
					await forecast_task
					
			elif (("who" in command or "was" in command or "what" in command  or ("search" in command and "youtube" not in command)) and ("date" not in command)):
				wiki_command=""
				if ("who" in command):
					wiki_command=command.split("who was ")[1]
				elif ("what" in command):
					wiki_command=command.split("what is ")[1]
				elif ("was" in command):
					wiki_command=command.split("was ")
				elif ("for" in command):
					wiki_command=command_search
				wiki_task=asyncio.create_task(Wikipedia_show.main(self, wiki_command.replace(" ","_"), tabcontrol))
				await wiki_task
				

			elif ("youtube" in command):
				if ("search" in command):
					yt_task=asyncio.create_task(yt_search(self, command_search, tabcontrol))
					await yt_task

			elif ("calibration" in command):
				calib_task = asyncio.create_task(Calibrate.main(self, tabcontrol))
				await calib_task

			elif ("news" in command):
				news_task=asyncio.create_task(display_news.main(self, show_news, tabcontrol))
				await news_task
			
			elif ("home" in command):
				for t in tabcontrol.tabs():
					if (t>0):
						tabcontrol.forget(t)
			
			elif ("close" in command):
				tabcontrol.forget(len(tabcontrol.tabs())-1)

			elif ("next" in command):
					processes=Work_with_files.read_process_from_file()
					p_name=''
					p_id=''
					for name, value in processes.items():
						p_name=name
						p_id=value
					if("Open_news" in p_name):
						Open_news=subprocess.Popen(["python3", "news.py", displayed])
						Work_with_files.print_process_to_file(str(Open_news.pid), "Open_news")
						os.kill(int(p_id), signal.SIGKILL)
						Work_with_files.remove_process_from_file(p_id)
			elif (command in numbers_int or command in numbers_string or command in position):
				get_position=0
				if (command in numbers_int):
					get_position=numbers_int.index(command) + 1
				elif (command in numbers_string):
					get_position=numbers_string.index(command) + 1
				elif (command in position):
					get_position=position.index(command) + 1
				
				print(get_position)

				yt_stream_task=asyncio.create_task(Video.main(self, get_position, tabcontrol))
				await yt_stream_task
			#else:
			#	asistant.jarvis(command)