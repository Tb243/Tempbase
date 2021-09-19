from hal.device import Device
import RPi.GPIO as GPIO
import time

class pump(Device):

	def __init__(self, pumpPin): 
		self.name = "PUMP"
		self.isVirtual = False
		self.servoPin = pumpPin

	def validateConfig(self):
		return True

	def setup(self):
		GPIO.setup(self.pumpPin, GPIO.OUT)
  
	def destroy(self):
		GPIO.cleanup()

	def read(self):
		pass

	def run(self):
		GPIO.output(self.pumpPin, 1)
		time.sleep(0.5)
		GPIO.output(self.pumpPin, 0)

