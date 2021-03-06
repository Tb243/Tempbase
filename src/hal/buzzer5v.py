from hal.device import Device
import RPi.GPIO as GPIO
import time

class Buzzer5v(Device):

	def __init__(self, buzzerPin):
		self.name = "BUZZER5V"
		self.isVirtual = False
		self.buzzerPin = buzzerPin

	def validateConfig(self):
		return True
		
	def setup(self):
		GPIO.setup(self.buzzerPin, GPIO.OUT)

	def destroy(self):
		GPIO.cleanup()

	def read(self):
		pass

	def buzz(self, timeLength):
		GPIO.output(self.buzzerPin, 1)
		time.sleep(timeLength)
		GPIO.output(self.buzzerPin, 0)

