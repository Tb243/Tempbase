from hal.device import Device
import time

class VirtualBUZZER5V(Device):
    
	def __init__(self, buzzerPin):
		self.name = "Virtual BUZZER5V"
		self.isVirtual = True
		self.buzzerPin = buzzerPin

	def validateConfig(self):
		return True

	def setup(self):
		time.sleep(2.0)

	def destroy(self):
		pass

	def read(self):
		pass

	def buzz(self):
		time.sleep(1)
