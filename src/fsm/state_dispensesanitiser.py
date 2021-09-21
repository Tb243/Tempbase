from fsm.state import FsmState
from config import config
import os
import time
from notifications.notify import Notifications
from notifications.notify_sms import SMSNotify
from config import config

VIRTUAL_MODE = True if os.environ.get("virtualMode") == "on" else False

if VIRTUAL_MODE:
	from hal.virtual_pump import VirtualPUMP as PUMP
	from hal.virtual_sen0368 import VirtualSEN0368 as SEN0368
else:
	from hal.pump import PUMP
	from hal.sen0368 import SEN0368

class StateDispenseSanitiser(FsmState):

	def __init__(self, fsm):
		self.identifier = "dispenseSanitiser"
		self.label = "Dispense Sanitiser"
		self.fsm = fsm
		self.pump = PUMP(config["hal"]["PUMP"]["pin"])
		self.liquidSensor = SEN0368(config["hal"]["SEN0368"]["pin"])
		self.smsNotifier = SMSNotify(config["twilio"]["systemNumber"], config["twilio"]["accountSID"], config["twilio"]["authTok"])
		self.emailNotifier = Notifications(config["email"]["transport"]["username"], config["email"]["transport"]["password"])

	def onEnterState(self, counter):
		self.counter = counter
		self.pump.setup()
		self.liquidSensor.setup()

	def onExitState(self):
		if self.liquidSensor.read() == 0:
			self.sendAlert()

	def main(self):
		self.pump.run()
		time.sleep(2)
		self.fsm.transitionState("measureTemperature", self.counter)

	def sendAlert(self):
		if len(config["twilio"]["numberTo"]) > 0:
			for recipient in config["twilio"]["numberTo"]:
				try:
					self.log("SMS notify " + recipient)
					self.smsNotifier.smsRefill(recipient)
					self.log("Empty notification SMS sent")
				except:
					self.log("Error sending SMS notification")
		
		if len(config["email"]["recipients"]) > 0:
			for recipient in config["email"]["recipients"]:
				try:
					self.log("Email notify " + recipient)
					self.emailNotifier.sendRefill(recipient)
					self.log("Empty notification email sent")
				except:
					self.log("Error sending email notifications")       
