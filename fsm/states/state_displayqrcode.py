from states import state
import time

class StateDisplayQrCode(state.FsmState):

	def __init__(self, fsm):
		self.identifier = "displayQrCode"
		self.label = "Display QR Code"
		self.fsm = fsm

	def onEnterState(self, args=None):
		print("Entering the display QR code state")
		

	def onExitState(self):
		print("Leaving the display QR code state")

	def main(self):
		#display qr code
		print("QR Code being displayed")
		#wait 10 seconds
		print("waiting 10 seconds")
		time.sleep(10)
		self.fsm.transitionState("waitForHand")
