from devices.device import Device
import time

class VirtualFS90R(Device):

	def __init__(self, servoPin=None): 
		self.name = "Virtual FS90R"
		self.isVirtual = True
		self.servoPin = servoPin

	def validateConfig(self):
		return True 

	def setup(self):
		time.sleep(2.0)
  
	def destroy(self):
		pass

	def read(self):
		pass
	
	def turn(self):
		time.sleep(1)

