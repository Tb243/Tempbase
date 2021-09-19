from hal.device import Device
import time

class VirtualPUMP(Device):

	def __init__(self, pumpPin): 
		self.name = "Virtual PUMP"
		self.isVirtual = True
		self.servoPin = pumpPin

	def validateConfig(self):
		return True 

	def setup(self):
		time.sleep(2.0)
  
	def destroy(self):
		pass

	def read(self):
		pass
	
	def run(self):
		time.sleep(1)

