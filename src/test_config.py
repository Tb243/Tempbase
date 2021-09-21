import unittest
from config import config

class DeviceTests(unittest.TestCase):

	def test_has_qr_code(self):
		self.assertTrue("QRCodeValue" in config)
		self.assertTrue(len(config["QRCodeValue"]) > 0)

	def test_email_configuration(self):
		self.assertTrue("email" in config)

		self.assertTrue("transport" in config["email"])
		self.assertTrue("smtpServer" in config["email"]["transport"])
		self.assertTrue("smtpPort" in config["email"]["transport"])
		self.assertTrue(isinstance(config["email"]["transport"]["smtpPort"], int))
		self.assertTrue("username" in config["email"]["transport"])
		self.assertTrue("password" in config["email"]["transport"])
		self.assertTrue(len(config["email"]["transport"]["password"]) > 0)

		self.assertTrue("recipients" in config["email"])
		self.assertTrue(isinstance(config["email"]["recipients"], list))

	def test_twilio_configuration(self):
		self.assertTrue("twilio" in config)

		self.assertTrue("accountSID" in config["twilio"])
		self.assertTrue("authTok" in config["twilio"])
		self.assertTrue("numberTo" in config["twilio"])
		self.assertTrue(isinstance(config["twilio"]["numberTo"], list))

	def test_hal(self):
		self.assertTrue("hal" in config)

	def test_hcsr04(self):
		self.assertTrue("HCSR04" in config["hal"])
		self.assertTrue("echoPin" in config["hal"]["HCSR04"])
		self.assertTrue(isinstance(config["hal"]["HCSR04"]["echoPin"], int))
		self.assertTrue("triggerPin" in config["hal"]["HCSR04"])
		self.assertTrue(isinstance(config["hal"]["HCSR04"]["triggerPin"], int))

	def test_buzzer(self):
		self.assertTrue("BUZZER" in config["hal"])
		self.assertTrue("pin" in config["hal"]["BUZZER"])
		self.assertTrue(isinstance(config["hal"]["BUZZER"]["pin"], int))

	def test_fs90r(self):
		self.assertTrue("FS90R" in config["hal"])
		self.assertTrue("pin" in config["hal"]["FS90R"])
		self.assertTrue(isinstance(config["hal"]["FS90R"]["pin"], int))

	def test_sen0368(self):
		self.assertTrue("SEN0368" in config["hal"])
		self.assertTrue("pin" in config["hal"]["SEN0368"])
		self.assertTrue(isinstance(config["hal"]["SEN0368"]["pin"], int))

	def test_health(self):
		self.assertTrue("health" in config)
		self.assertTrue("maxTemperatureThreshold" in config["health"])
		self.assertTrue(isinstance(config["health"]["maxTemperatureThreshold"], int))


if __name__ == "__main__":
    unittest.main(verbosity=2)