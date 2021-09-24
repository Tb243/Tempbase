import os
from fsm.state import FsmState
import time
from notifications.notify import Notifications
from notifications.notify_sms import SMSNotify
from config import config

VIRTUAL_MODE = True if os.environ.get("virtualMode") == "on" else False

if VIRTUAL_MODE:
	from hal.virtual_buzzer5v import VirtualBUZZER5V as Buzzer5v
else:
	from hal.buzzer5v import Buzzer5v

class StateRejectUser(FsmState):

	def __init__(self, fsm):
		self.identifier = "rejectUser"
		self.label = "Reject User"
		self.fsm = fsm
		self.buzzer = Buzzer5v(26)
		self.smsNotifier = SMSNotify(config["twilio"]["numberFrom"], config["twilio"]["accountSID"], config["twilio"]["authTok"])
		self.emailNotifier = Notifications(config["email"]["transport"]["username"], config["email"]["transport"]["password"])
		
	def onEnterState(self, args):
		self.temperature = args[0]
		self.counter = args[1]
		self.buzzer.setup()

	def onExitState(self):
		pass

	def main(self):
		self.log("Displaying red cross")
		self.buzzer.buzz(0.5)

		if self.counter == 1:
			self.log("Please measure your temperature again")
			time.sleep(7)
			self.fsm.transitionState("measureTemperature", self.counter)
		else:
			self.log("Temperature is too high please take a COVID test and isolate")
			self.sendAlert()
			time.sleep(7)
			self.fsm.transitionState("waitForHand")
			
	def sendAlert(self):
		if len(config["twilio"]["numberTo"]) > 0:
			for recipient in config["twilio"]["numberTo"]:
				try:
					self.log("SMS notify " + recipient)
					self.smsNotifier.smsTemp(recipient, round(self.temperature, 1))
					self.log("Santise SMS sent")
				except:
					self.log("Error sending SMS notification")
		
		if len(config["email"]["recipients"]) > 0:
			for recipient in config["email"]["recipients"]:
				try:
					self.log("Email notify " + recipient)
					self.emailNotifier.sendTemp(recipient, round(self.temperature, 1))
					self.log("Sanitise email sent")
				except:
					self.log("Error sending email notifications")
