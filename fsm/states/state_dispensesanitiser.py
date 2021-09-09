from states import state

class StateDispenseSanitiser(state.FsmState):

	def __init__(self, fsm):
		self.identifier = "dispenseSanitiser"
		self.label = "Dispense Sanitiser"
		self.fsm = fsm

	def onEnterState(self, args=None):
		print("Entering the dispense sanitiser state")
		# src04.setup()

	def onExitState(self):
		print("Leaving the dispense sanitiser state")

	def main(self):
		while True:
			# turn = fs90r.turn()
			turn = float(input("Enter 1 for sanitiser to dispense: "))
			if turn < 1:
				break

		self.fsm.transitionState("measureTemperature")
