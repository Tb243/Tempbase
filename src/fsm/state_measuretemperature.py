from fsm.state import FsmState
import os
import time

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

        timeStart = time.time()
        startTemperature = self.temperatureSensor.read()

        # Spend no more than one second measuring the temperature.
        while (time.time() - timeStart) < 1.0:
            read = self.temperatureSensor.read()
            difference = read - startTemperature

            # If the temperature value has increased more than ten percent, break the loop early.
            if startTemperature > 0 and (difference / startTemperature) > 0.1:
                break

            time.sleep(0.1)


        self.counter += 1
        self.fsm.setStateData("temperatureMeasurement", read)
        self.fsm.setStateData("attemptCounter", self.counter)
        
        self.fsm.transitionState("processAndStoreTemperature", [read, self.counter])
