from gtts import gTTS
import time
import pygame
from helpers import *

class Speech:
	"""used for generating and playing speech from text"""

	def __init__(self, text = "", path = 'speech.mp3'):
		self.text = text
		self.lang = 'en'
		self.file = path
		pygame.mixer.init()

	def talk(self):
		speech = gTTS(text=self.text, lang=self.lang)
		speech.save(self.file)
		pygame.mixer.music.load(self.file)
		pygame.mixer.music.play()
		wait()


class Player:
	"""used for playing audio files"""
	def __init__(self, path = ''):
		pygame.mixer.init()
		pygame.mixer.music.load(path)

	def play(self):
		pygame.mixer.music.play()
		wait()

		