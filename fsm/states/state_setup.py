from states import state
import time

class StateSetup(state.FsmState):

	def __init__(self, fsm):
		self.identifier = "setup"
		self.label = "Setup"
		self.fsm = fsm

	def main(self):
		print("Setting up...")
		self.fsm.transitionState("waitForHand")