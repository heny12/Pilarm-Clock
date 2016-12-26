# play 1st minute of vivaldis spring
# say greeting
# say time
# read the weather
# top 3 news headlines
# continue playing spring

from speech import Speech, Player
from helpers import *
import pygame
	
name = 'Henry'
greeting = get_greeting(name)
weather = get_weather()
headlines = get_headlines(3)

opening = Player('vivaldi.mp3')
closing = Player('vivaldi2.mp3')
speech = Speech(greeting + weather + headlines)

# opening.play()
speech.talk()
# closing.play()
