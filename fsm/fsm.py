from states import state_setup

class Fsm:

	def __init__(self):
		self.states = {}
		self.currentState = None

	def addState(self, state):
		self.states[state.identifier] = state

	def transitionState(self, nextState, args=None):
		if not nextState in self.states:
			raise("Tried to transition to state '%s' which is an unknown state identifier" % nextState)

		if self.currentState and self.currentState in self.states:
			self.states[self.currentState].onExitState()

		self.currentState = nextState
		self.states[self.currentState].onEnterState(args)

	def spin(self):
		if not self.currentState:
			raise("FSM cannot spin without a current state")

		if not self.currentState in self.states:
			raise("Tried to spin in state '%s' which is an unknown state identifier" % self.currentState)

		self.states[self.currentState].main()
		self.spin()

if __name__ == "__main__":
	fsm = Fsm()
	fsm.addState(state_setup.StateSetup(fsm))
	fsm.transitionState("setup")
	
	fsm.spin()