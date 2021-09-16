import os
from fsm.state import FsmState

VIRTUAL_MODE = True if os.environ.get("virtualMode") == "on" else False

if VIRTUAL_MODE:
    from hal.virtual_mlx90614 import VirtualMLX90614 as MLX90614
else:
    from hal.mlx90614 import MLX90614

class StateMeasureTemperature(FsmState):

    def __init__(self, fsm):
        self.identifier = "measureTemperature"
        self.label = "Measure Temperature"
        self.fsm = fsm
        self.temperatureSensor = MLX90614()

    def onEnterState(self, counter):
        self.counter = counter
        self.temperatureSensor.setup()

    def onExitState(self):
        pass

    def main(self):
        read = self.temperatureSensor.read()
        #read = float(input("Enter temperature value: "))
        self.counter += 1
        #print("Counter is: ", self.counter)
        self.fsm.transitionState("processAndStoreTemperature", [read, self.counter])
