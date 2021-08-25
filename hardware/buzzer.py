import RPi.GPIO as GPIO
import time

class Buzzer:

	def __init__(self, buzzerPin):
		self.buzzerPin = buzzerPin
		GPIO.setup(self.buzzerPin, GPIO.OUT)	

	def on(self):
    	GPIO.output(self.buzzerPin, 1)

	def off(self):
    	GPIO.output(self.buzzerPin, 0)
	
	def buzz_for(self, seconds):
		self.on()
		time.sleep(seconds)
		self.off()