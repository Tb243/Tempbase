from states import state

class StateMeasureTemperature(state.FsmState):

	def __init__(self, fsm):
		self.identifier = "measureTemperature"
		self.label = "Measure Temperature"
		self.fsm = fsm

	def onEnterState(self, args=None):
		print("Entering the measure temperature state")
		# mlx90614.setup()

	def onExitState(self):
		print("Leaving the measure temperature state")

	def main(self):
		while True:
			# turn = mlx90614.read()
			read = float(input("Enter value under 37.6 for temperature: "))
			if read < 37.6:
				break

		self.fsm.transitionState("processAndStoreTemperature")
