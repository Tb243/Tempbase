from devices.device import Device
import random

class VirtualMLX90614(Device):

	def __init__(self):
		self.name = "Virtual MLX90614"
		self.isVirtual = True

	def validateConfig(self):
		return True

	def setup(self):
		pass

	def destroy(self):
		pass

	def read(self):
		return random.uniform(-20, 100)
