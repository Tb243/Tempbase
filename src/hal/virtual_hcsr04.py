from hal.device import Device
import random
import time

class VirtualHCSR04(Device):

	def __init__(self, echoPin=None, triggerPin=None):
		self.name = "Virtual HCSP04"
		self.isVirtual = True
		self.echoPin = echoPin
		self.triggerPin = triggerPin

	def validateConfig(self):
		return True if (self.echoPin != None and self.triggerPin != None) else False

	def setup(self):
		# No pins need to be set up as this is a virtual device.
		time.sleep(2.0)

	def destroy(self):
		# No pins need to be disabled as this is a virtual device.
		pass

	def read(self, timeout=1.0):
		# Since this is a virtual device, we just generate a fake 
		# value to emulate a sensorreading.
		time.sleep(0.00001)
		return random.uniform(0.5, 15.0)