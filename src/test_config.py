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


if __name__ == "__main__":
    unittest.main(verbosity=2)