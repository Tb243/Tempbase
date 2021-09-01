import unittest
from devices import hcsp04
from devices import virtual_hcsp04

ECHO_PIN = 13
TRIGGER_PIN = 6

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



class TestPhysicalHCSP04(unittest.TestCase, DeviceTests):
	def setUp(self):
		self.device = hcsp04.HCSP04(ECHO_PIN, TRIGGER_PIN)
		try:
			self.device.setup()
		except:
			pass

class TestVirtualHCSP04(unittest.TestCase, DeviceTests):

	def setUp(self):
		self.device = virtual_hcsp04.VirtualHCSP04(ECHO_PIN, TRIGGER_PIN)

	def testRead(self):
		try:
			value = self.device.read()
			self.assertTrue(value >= 0.5 and value <= 15.0)
		except:
			self.fail("read() has not been implemented for device %s" % self.device.name)


if __name__ == "__main__":
	unittest.main(verbosity=2)