from fsm.state import FsmState
from config import config
import time

class StateProcessAndStoreTemp(FsmState):

    def __init__(self, fsm):
        self.identifier = "processAndStoreTemperature"
        self.label = "Process and store temperature"
        self.fsm = fsm

    def onEnterState(self, args):
        self.temperature = args[0]
        self.counter = args[1]
        
    def onExitState(self):
        pass

    def main(self):
        # add read (temp) value to database
        if self.temperature < config["health"]["maxTemperatureThreshold"]:
            #display green tick
            self.log("Your temperature is: %d" % self.temperature)
            self.log("Green Tick being displayed")
            time.sleep(2)
            self.fsm.transitionState("displayQrCode")
        else : 
            self.log("Your temperature is: %d" % self.temperature)
            self.fsm.transitionState("rejectUser", self.counter)
        