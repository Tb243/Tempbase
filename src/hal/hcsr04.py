from hal.device import Device
import RPi.GPIO as GPIO
import time

class HCSR04(Device):

	def __init__(self, echoPin=None, triggerPin=None):
		self.name = "HCSR04"
		self.isVirtual = False
		self.echoPin = echoPin
		self.triggerPin = triggerPin

	def validateConfig(self):
		if self.echoPin != None and self.triggerPin != None:
			return True

	def setup(self):
		GPIO.setup(self.echoPin, GPIO.IN)
		GPIO.setup(self.triggerPin, GPIO.OUT)
		GPIO.output(self.triggerPin, 0)
		time.sleep(2.0)

	def destroy(self):
		GPIO.cleanup()

	def read(self):
		GPIO.output(self.triggerPin, 1)
		time.sleep(0.00001)
		GPIO.output(self.triggerPin, 0)

		pulseStart = time.time()
		while GPIO.input(self.echoPin) == 0:
			pulseStart = time.time()

		pulseEnd = time.time()
		while GPIO.input(self.echoPin) == 1:
			pulseEnd = time.time()

		return (pulseEnd - pulseStart) * 17150
