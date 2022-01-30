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
open_processes=[]
		
class Do_for_command:
	def __call__(args):
			try: 
				print('test:     '+args)
			except:
				print('')
	def __init__(self, command, user, displayed, previous_search, tabcontrol):

		print('WE HAVE IT')
		print(type(tabcontrol))
		numbers_int=["1","2","3","4","5","6","7","8","9","10"]
		numbers_string=["one","two","three","four","five","six","seven","eight","nine","ten"]
		position=["first", "second","thirth","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
		
		

		self.show_news=displayed
		self.tabcontrol=tabcontrol
		command=command.lower()
		command_search=""
		if (" for " in command):
			command_search=command.split(" for ")[1]
		if (command!=""):
			if("forecast" in command or "weather" in command):
				if (command_search==""):
					Open_forecast=subprocess.Popen(["python3","weather.py"], 'today')
					Work_with_files.print_process_to_file(str(Open_forecast.pid), "Open_forecast")
					
				else:
					Open_forecast=subprocess.Popen(["python3","weather.py",command_search])
					Work_with_files.print_process_to_file(str(Open_forecast.pid), "Open_forecast")
					
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
				w=Wikipedia_show(wiki_command.replace(" ","_"), self.tabcontrol)
				#Open_wiki=subprocess.Popen(["python3","wikipedia_window.py",wiki_command.replace(" ","_")])
				#Work_with_files.print_process_to_file(str(Open_wiki.pid), "Open_wiki")
				

			elif ("youtube" in command):
				if ("search" in command):
					yt=yt_search(command_search, self.tabcontrol)
					#Open_yt_search=subprocess.Popen(["python3","youtube.py", command_search])
					#open_processes.append("Open_yt_search")
					#Work_with_files.print_process_to_file(str(Open_yt_search.pid), "Open_yt_search")
				elif ("play" in command):
					Open_yt=subprocess.Popen(["python3","youtube_stream.py", command])
					open_processes.append("Open_yt")
					Work_with_files.print_process_to_file(str(Open_yt.pid), "Open_yt")

			elif ("calibration" in command):
				Open_calibrate=subprocess.Popen(["python3", "calibrate.py", user])
				Work_with_files.print_process_to_file(str(Open_calibrate.pid), "Open_calibrate")

			elif ("news" in command):
				n=display_news(self.show_news, self.tabcontrol)
				#Open_news=subprocess.Popen(["python3", "news.py", str(show_news)])
				#Work_with_files.print_process_to_file(str(Open_news.pid), "Open_news")
				
			elif("picture" in command):
				if ("take" in command):
						take_pic=subprocess.Popen(["python3","take_picture.py",user])
						open_processes.append("take_pic:"+str(take_pic.pid))
			elif("timer" in command):
				start_timer=subprocess.Popen(["python3","timer.py",command_search])
				Speaking.to_say("Setting a timer for " + str(command_search))
				Work_with_files.print_process_to_file(str(start_timer.pid), "Start_timer")
			
			elif ("home" in command):
				processes=Work_with_files.read_process_from_file()
				print(type(processes))
				for name, value in processes.items():
					print(name+':'+str(value))
					try:
						os.kill(int(value), signal.SIGKILL)
					except:
						continue
				Work_with_files.remove_all_processes_from_file()
				for t in self.tabcontrol.tabs():
					if (t>0):
						self.tabcontrol.forget(t)
			
			elif ("close" in command):
				'''processes=Work_with_files.read_process_from_file()
				id_to_kill=''
				for name, value in processes.items():
						id_to_kill=value
						print(id_to_kill)
				os.kill(int(id_to_kill), signal.SIGKILL)
				Work_with_files.remove_process_from_file(id_to_kill)'''
				self.tabcontrol.forget(len(self.tabcontrol.tabs())-1)

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
				#str_to_search=previous_search.split('for ')[1].replace(' ','_')
				get_position=0
				if (command in numbers_int):
					get_position=numbers_int.index(command) + 1
				elif (command in numbers_string):
					get_position=numbers_string.index(command) + 1
				elif (command in position):
					get_position=position.index(command) + 1
				
				print(get_position)

				yt_stream=Video(get_position, self.tabcontrol)
				'''processes=Work_with_files.read_process_from_file()
				p_name=''
				p_id=''
				for name, value in processes.items():
					p_name=name
					p_id=value
				if ("Open_yt_search" in p_name):
					str_to_search=previous_search.split('for ')[1].replace(' ','_')
					Open_yt=subprocess.Popen(["python3","youtube_stream.py", str_to_search, command])
					Work_with_files.print_process_to_file(str(Open_yt.pid), "Open_yt")'''
			#else:
			#	asistant.jarvis(command)