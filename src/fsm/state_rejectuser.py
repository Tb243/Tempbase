import os
from fsm.state import FsmState
import time

VIRTUAL_MODE = True if os.environ.get("virtualMode") == "on" else False

if VIRTUAL_MODE:
    from hal.virtual_buzzer5v import VirtualBUZZER5V as Buzzer5v
else:
    from hal.buzzer5v import Buzzer5v

class StateRejectUser(FsmState):

    def __init__(self, fsm):
        self.identifier = "rejectUser"
        self.label = "Reject User"
        self.fsm = fsm
        self.buzzer = Buzzer5v(26)
        
    def onEnterState(self, counter):
        self.counter = counter
        self.buzzer.setup()

    def onExitState(self):
        pass

    def main(self):
        #display red cross
        self.log("Displaying red cross")
        time.sleep(5)
        if self.counter == 1:
            self.buzzer.buzz(0.5)
            self.log("BUZZ")
            self.log("Please measure your temperature again")
            time.sleep(2)
            self.fsm.transitionState("measureTemperature", self.counter)
        else:
            self.log("Temperature is too high please take a COVID test and isolate")
            self.buzzer.buzz(0.5)
            self.log("BUZZ")
            time.sleep(2)
            # send alert to device owner
            self.fsm.transitionState("waitForHand")
