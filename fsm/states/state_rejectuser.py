from states import state
import time

class StateRejectUser(state.FsmState):

	def __init__(self, fsm):
		self.identifier = "rejectUser"
		self.label = "Reject User"
		self.fsm = fsm

	def onEnterState(self, args=None):
		print("Entering the reject user state")
		

	def onExitState(self):
		print("Leaving the reject user state")

	def main(self):
		#display red cross
		print("Displaying red cross")
		time.sleep(5)
		#if temperature has already been read then
		print("Please measure your temperature again")
		self.fsm.transitionState("measureTemperature")
		#else
		#display message saying to get a COVID test
		# send alert to device owner
		#self.fsm.transitionState("waitForHand")
