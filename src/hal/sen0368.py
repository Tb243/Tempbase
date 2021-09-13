from hal.device import Device
import RPi.GPIO as GPIO
import time


class SEN0368(Device):

	def __init__(self, liquidPin):
		self.name = "SEN0368"
		self.isVirtual = False
  		self.liquidPin = liquidPin

	def validateConfig(self):
		return True

	def setup(self):
    	GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.liquidPin, GPIO.IN)

	def destroy(self):
		GPIO.cleanup()

	def read(self):
        time.sleep(1)
		return GPIO.input(self.liquidPin)

