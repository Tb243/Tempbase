import unittest
import sys
from devices import virtual_hcsr04

# Physical devices should each be wrapped in try except blocks
try:
	from devices import hcsr04
except:
	pass

HCSR04_ECHO_PIN = 13
HCSR04_TRIGGER_PIN = 6

class DeviceTests:
	def testSetup(self):
		try:
			self.device.setup()
		except:
			self.fail("setup() has not been implemented for device %s" % self.device.name)

	def testValidateConfig(self):
		try:
			self.assertTrue(self.device.validateConfig())
		except:
			self.fail("validateConfig() has not been implemented for device %s" % self.device.name)

	def testRead(self):
		try:
			self.device.read()
		except:
			self.fail("read() has not been implemented for device %s" % self.device.name)


# This needs to be wrapped to prevent tests from crashing on
# devices that don't have RPi.GPIO installed.
if "hcsr04" in sys.modules:
	class TestPhysicalHCSR04(unittest.TestCase, DeviceTests):
		def setUp(self):
			self.device = hcsr04.HCSR04(HCSR04_ECHO_PIN, HCSR04_TRIGGER_PIN)
			try:
				self.device.setup()
			except:
				pass

class TestVirtualHCSR04(unittest.TestCase, DeviceTests):

	def setUp(self):
		self.device = virtual_hcsr04.VirtualHCSR04(HCSR04_ECHO_PIN, HCSR04_TRIGGER_PIN)

	def testRead(self):
		try:
			value = self.device.read()
			self.assertTrue(value >= 0.5 and value <= 15.0)
		except:
			self.fail("read() has not been implemented for device %s" % self.device.name)


if __name__ == "__main__":
	unittest.main(verbosity=2)