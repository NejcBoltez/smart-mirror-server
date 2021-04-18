from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen


#browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#browser.get('https://www.delo.si/novice/svet/odprte-obcinske-meje-in-vse-trgovine-ucenci-v-soli-ali-na-pocitnicah/')
website=urlopen('https://www.delo.si/novice/svet/odprte-obcinske-meje-in-vse-trgovine-ucenci-v-soli-ali-na-pocitnicah/').read()
#content=browser.page_source
#print(website)
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
#print(soup)
''' 
https://stackoverflow.com/questions/22476112/using-chromedriver-with-selenium-python-ubuntu


Installed the chromium-chromedriver:

sudo apt-get install chromium-chromedriver
Adding the path to the selenium line:

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
Note that this opens Chromium and not Chrome. Hope it was helpful.'''
