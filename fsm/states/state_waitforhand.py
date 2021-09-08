from states import state

class StateWaitForHand(state.FsmState):

	def __init__(self, fsm):
		self.identifier = "waitForHand"
		self.label = "Wait for hand"
		self.fsm = fsm

	def onEnterState(self, args=None):
		print("Entering the wait for hand state")
		# src04.setup()

	def onExitState(self):
		print("Leaving the wait for hand state")

	def main(self):
		while True:
			# distance = src04.read()
			distance = float(input("Enter distance: "))
			if distance < 10:
				break

		self.fsm.transitionState("dispenceSanitiser")
