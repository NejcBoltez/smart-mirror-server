from django.shortcuts import render
from .working_with_files import Work_with_files

loginedUser = 'Nejc'
youtubeData = []

newsProviders = ["Google","24ur","rtvslo","siol","racunalniske novice"]

#Return the Home page
def homePage(request,test):
	global youtubeData
	newsData = 1
	context = { 'data': newsData, 'values':youtubeData}
	print(test)
	if request.method == "GET":
		print(request.path)
		context['data'] = test
		if ("home" in test):
			context['weatherData'] = Work_with_files.read_weather_main()
			context['newsData'] = Work_with_files.read_news_data()['articles']
		elif ("weather" in test):
			context['dates'] = Work_with_files.get_all_dates_for_weather()
			context['values'] = Work_with_files.read_weather_data()
		elif ("news" in test):
			context['values'] = Work_with_files.read_news_data()['articles']
		elif("wikipedia" in test):
			try:
				searchFor = request.META['QUERY_STRING'].replace("&","").split("=")[1]
				context['values'] = Work_with_files.get_wiki_data(searchFor)
			except Exception as e:
				print("ERROR: "+str(e))
				context['values'] = Work_with_files.get_wiki_data("Bill_gates")
		elif ("ytSearch" in test):
			try:
				searchFor = request.META['QUERY_STRING'].replace("&","").split("=")[1]
				context['values'] = Work_with_files.get_yt_data(searchFor)['videos']
			except Exception as e:
				context['values'] = Work_with_files.getSaved_yt_data()['videos']
		elif ("ytStream" in test):
			try:
				streamIndex = request.META['QUERY_STRING'].replace("&","").split("=")[1]
				print(streamIndex)
				context['values'] = Work_with_files.stream_youtube(int(streamIndex))
			except Exception as e:
				context['values'] = Work_with_files.stream_youtube(0)
	return render(request,'smartmirror_django/SmartMirrorTemplate/home.html',context)