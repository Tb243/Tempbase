from hal.device import Device
import RPi.GPIO as GPIO
import time

class FS90R(Device):

	def __init__(self, servoPin): 
		self.name = "FS90R"
		self.isVirtual = False
		self.servoPin = servoPin

	def validateConfig(self):
		return True

	def setup(self):
		GPIO.setup(self.servoPin, GPIO.OUT)
  
	def destroy(self):
		GPIO.cleanup()

	def read(self):
		pass

	def turn(self):
		pwm = GPIO.PWM(self.servoPin, 50)
		pwm.start(0)
		pwm.ChangeDutyCycle(20.4)
		time.sleep(1)
		pwm.stop()
