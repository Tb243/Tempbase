import unittest
import sys
from hal import virtual_hcsr04
from hal import virtual_mlx90614
from hal import virtual_buzzer5v
from hal import virtual_fs90r
from hal import virtual_sen0368
from config import config

# Physical devices should each be wrapped in try except blocks
try:
    from hal import hcsr04
    from hal import mlx90614
    from hal import buzzer5v
    from hal import fs90r
    from hal import sen0368
except:
    pass

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
            self.device = hcsr04.VirtualHCSR04(config["hal"]["HCSR04"]["echoPin"], config["hal"]["HCSR04"]["triggerPin"])
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

if "buzzer5v" in sys.modules:
    class TestPhysicalBUZZER5V(unittest.TestCase, DeviceTests):
        def setUp(self):
            self.device = buzzer5v.BUZZER5V()
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
        self.device = virtual_hcsr04.VirtualHCSR04(config["hal"]["HCSR04"]["echoPin"], config["hal"]["HCSR04"]["triggerPin"])

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
            self.assertTrue(value >= 35 and value <= 45)
        except:
            self.fail("read() has not been implemented for device %s" % self.device.name)

class TestVirtualBuzzer5v(unittest.TestCase, DeviceTests):
    
    def setUp(self):
        self.device = virtual_buzzer5v.VirtualBUZZER5V()
    
    def testBuzz(self):
        try:
            value = self.device.buzz()
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
            self.assertTrue(value >= 0 and value <= 1)
        except:
            self.fail("read() has not been implemented for device %s" % self.device.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)