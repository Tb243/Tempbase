from fsm.state import FsmState
from database.model.temperatureEventModel import TemperatureEventModel
from config import config
import os
import time

DEBUG_MODE = True if os.environ.get("debugMode") == "on" else False

class StateProcessAndStoreTemp(FsmState):

    def __init__(self, fsm):
        self.identifier = "processAndStoreTemperature"
        self.label = "Process and store temperature"
        self.fsm = fsm
        self.temperatureModel = TemperatureEventModel(DEBUG_MODE)

    def onEnterState(self, args):
        self.temperature = args[0]
        self.counter = args[1]
        
    def onExitState(self):
        pass

    def main(self):
        if self.temperature < config["health"]["maxTemperatureThreshold"]:
            self.temperatureModel.recordTemperature(self.temperature, True)
            #display green tick
            self.log("Your temperature is: %d" % self.temperature)
            self.log("Green Tick being displayed")
            time.sleep(2)
            self.fsm.transitionState("displayQrCode")
        else : 
            self.temperatureModel.recordTemperature(self.temperature, False)
            self.log("Your temperature is: %d" % self.temperature)
            self.fsm.transitionState("rejectUser", self.counter)
        