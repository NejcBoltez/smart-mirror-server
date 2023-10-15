from django.shortcuts import render

#Return the Home page
def homePage(request):
	return render(request,'smartmirror_django/TVapp/home.html')