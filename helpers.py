import pygame
import datetime
import requests
import json
from pprint import pprint

def wait():
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)

def get_greeting(name):
	hour = datetime.datetime.now().hour
	greeting = ''
	if hour < 12:
		greeting = 'Good Morning '
	if hour < 18:
		greeting = 'Good Afternoon '
	else:
		greeting = 'Good Evening '
	return greeting + name + '.'

def get_weather():
	# TODO based on location
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Seattle&APPID=9935847f235b2e508070cc9e226bc8aa&units=imperial')
	j = r.json()
	temperature = j['main']['temp']
	temphi = j['main']['temp_max']
	templo = j['main']['temp_min']
	description = j['weather'][0]['main']
	cloud = j['clouds']['all']
	return "The current weather for your location is %s with a temperature of %s degrees. Todays high temperature is %s and low temperature is %s. Cloud coverage is %s percent." % (description, temperature, temphi, templo, cloud)

def get_headlines(count):
	headlines = []
	r = requests.get('https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey=1ca99d1f4bc3451b930b177af45bf272')
	articles = r.json()['articles']
	for i in range(count):
		title = articles[i]["title"]
		description = articles[i]["description"]
		headlines.append(title + '. ' + description)
	return 'Here are your news stories for today:' + str(' Next Article: '.join(headlines).encode("ascii", "ignore"))
