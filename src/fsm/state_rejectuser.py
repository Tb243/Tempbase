import os
from fsm.state import FsmState
import time

VIRTUAL_MODE = True if os.environ.get("virtualMode") == "on" else False

if VIRTUAL_MODE:
    from hal.virtual_buzzer5v import VirtualBUZZER5V as buzzer5v
else:
    from hal.buzzer5v import buzzer5v

class StateRejectUser(FsmState):

    def __init__(self, fsm):
        self.identifier = "rejectUser"
        self.label = "Reject User"
        self.fsm = fsm
        self.servoMotor = buzzer5v(26)
        
    def onEnterState(self, counter):
        self.counter = counter
        self.servoMotor.setup()

    def onExitState(self):
        pass

    def main(self):
        #display red cross
        self.log("Displaying red cross")
        time.sleep(5)
        if self.counter == 1:
            self.servoMotor.buzz()
            self.log("BUZZ")
            self.log("Please measure your temperature again")
            time.sleep(2)
            self.fsm.transitionState("measureTemperature", self.counter)
        else:
            self.log("Temperature is too high please take a COVID test and isolate")
            self.servoMotor.buzz()
            self.log("BUZZ")
            time.sleep(2)
            # send alert to device owner
            self.fsm.transitionState("waitForHand")
