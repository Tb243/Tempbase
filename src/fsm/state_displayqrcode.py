from fsm.state import FsmState
from config import config
import time

class StateDisplayQrCode(FsmState):

	def __init__(self, fsm):
		self.identifier = "displayQrCode"
		self.label = "Display QR Code"
		self.fsm = fsm

	def onEnterState(self, args=None):
		self.fsm.setStateData("QRCodeValue", config["QRCodeValue"])

	def onExitState(self):
		pass

	def main(self):
		self.log("QR Code being displayed")
		self.log("Waiting 10 seconds")
		time.sleep(10)
		self.fsm.transitionState("waitForHand")
