from fsm.state import FsmState
from config import config
import os
import time

VIRTUAL_MODE = True if os.environ.get("virtualMode") == "on" else False

if VIRTUAL_MODE:
    from hal.virtual_fs90r import VirtualFS90R as FS90R
    from hal.virtual_sen0368 import VirtualSEN0368 as SEN0368
else:
    from hal.fs90r import FS90R
    from hal.sen0368 import SEN0368

class StateDispenseSanitiser(FsmState):

    def __init__(self, fsm):
        self.identifier = "dispenseSanitiser"
        self.label = "Dispense Sanitiser"
        self.fsm = fsm
        self.servoMotor = FS90R(config["hal"]["FS90R"]["pin"])
        self.liquidSensor = SEN0368(config["hal"]["SEN0368"]["pin"])

    def onEnterState(self, counter):
        self.counter = counter
        self.servoMotor.setup()
        self.liquidSensor.setup()

    def onExitState(self):
        # If the liquid level is low, send alert to device owner
        if self.liquidSensor.read() == 0:
            self.sendAlert()

    def main(self):
        self.servoMotor.turn()
        time.sleep(2)
        self.fsm.transitionState("measureTemperature", self.counter)

    def sendAlert(self):
        # Send the alert to the device owner
        pass