import os
from fsm.state import FsmState
import time

VIRTUAL_MODE = True if os.environ.get("virtualMode") == "on" else False

class StateDisplayQrCode(FsmState):

	def __init__(self, fsm):
		self.identifier = "displayQrCode"
		self.label = "Display QR Code"
		self.fsm = fsm

	def onEnterState(self, args=None):
		pass

	def onExitState(self):
		pass

	def main(self):
		#display qr code
		self.log("QR Code being displayed")
		#wait 10 seconds
		self.log("waiting 10 seconds")
		time.sleep(10)
		self.fsm.transitionState("waitForHand")
