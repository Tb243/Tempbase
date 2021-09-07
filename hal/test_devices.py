import unittest
import sys
from devices import virtual_hcsr04
from devices import virtual_mlx90614
from devices import virtual_fs90r
from devices import virtual_sen0368

# Physical devices should each be wrapped in try except blocks
try:
    from devices import hcsr04
    from devices import mlx90614
    from devices import fs90r
    from devices import sen0368
except:
    pass

HCSR04_ECHO_PIN = 13
HCSR04_TRIGGER_PIN = 6
FS90R_SERVO_PIN = 12
SEN0368_LIQUID_PIN = 20

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

if "mlx90614" in sys.modules:
    class TestPhysicalMLX90614(unittest.TestCase, DeviceTests):
        def setUp(self):
            self.device = mlx90614.MLX90614()
            try:
                self.device.setup()
            except:
                pass
if "fs90r" in sys.modules:
    class TestPhysicalFS90R(unittest.TestCase, DeviceTests):
        def setUp(self):
            self.device = fs90r.FS90R()
            try:
                self.device.setup()
            except:
                pass
if "sen0368" in sys.modules:
    class TestPhysicalSEN0368(unittest.TestCase, DeviceTests):
        def setUp(self):
            self.device = sen0368.SEN0368()
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

class TestVirtualMLX90614(unittest.TestCase, DeviceTests):

    def setUp(self):
        self.device = virtual_mlx90614.VirtualMLX90614()

    def testRead(self):
        try:
            value = self.device.read()
            self.assertTrue(value >= -20 and value <= 100)
        except:
            self.fail("read() has not been implemented for device %s" % self.device.name)

class TestVirtualFS90R(unittest.TestCase, DeviceTests):
    
    def setUp(self):
        self.device = virtual_fs90r.VirtualFS90R()

    def testTurn(self):
        try:
            value = self.device.turn()
        except:
            self.fail("read() has not been implemented for device %s" % self.device.name)
class TestVirtualSEN0368(unittest.TestCase, DeviceTests):
    
    def setUp(self):
        self.device = virtual_sen0368.VirtualSEN0368()

    def testRead(self):
        try:
            value = self.device.read()
            self.assertTrue(value >= 0.5 and value <= 15.0)
        except:
            self.fail("read() has not been implemented for device %s" % self.device.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)