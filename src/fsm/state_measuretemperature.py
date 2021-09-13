from fsm.state import FsmState

class StateMeasureTemperature(FsmState):

	def __init__(self, fsm):
		self.identifier = "measureTemperature"
		self.label = "Measure Temperature"
		self.fsm = fsm

	def onEnterState(self, counter):
		print("Entering the measure temperature state")
		# mlx90614.setup()
		self.counter = counter

	def onExitState(self):
		print("Leaving the measure temperature state")

	def main(self):
		# turn = mlx90614.read()
		read = float(input("Enter temperature value: "))
		self.counter += 1
		#print("Counter is: ", self.counter)
		self.fsm.transitionState("processAndStoreTemperature", [read, self.counter])