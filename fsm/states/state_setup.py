from states import state

class StateSetup(state.FsmState):

	def __init__(self, fsm):
		self.identifier = "setup"
		self.label = "Setup"
		self.fsm = fsm

	def main(self):
		print("Setting up...")

		#Set up server
		#Set up database
		#Set up web browser (launch web browser)
		self.fsm.transitionState("waitForHand")