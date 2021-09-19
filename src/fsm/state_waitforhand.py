from fsm.state import FsmState
from config import config
from main import VIRTUAL_MODE
import time

if VIRTUAL_MODE:
    from hal.virtual_hcsr04 import VirtualHCSR04 as HCSR04
else:
    from hal.hcsr04 import HCSR04

class StateWaitForHand(FsmState):

    def __init__(self, fsm):
        self.identifier = "waitForHand"
        self.label = "Wait for hand"
        self.fsm = fsm
        self.hcsr04 = HCSR04(config["hal"]["HCSR04"]["echoPin"], config["hal"]["HCSR04"]["triggerPin"])

    def onEnterState(self, args=None):
        self.hcsr04.setup()

    def onExitState(self):
        pass

    def main(self):
        counter = 0
        while True:
            distance = self.hcsr04.read()
            self.fsm.setStateData("ultrasonicDistance", distance)
            self.log("Distance to hand: %f" % distance)
            if distance < 12:
                break
            time.sleep(2)


        self.fsm.transitionState("dispenseSanitiser", counter)
