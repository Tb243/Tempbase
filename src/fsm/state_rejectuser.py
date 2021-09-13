from fsm.state import FsmState
import time

class StateRejectUser(FsmState):

    def __init__(self, fsm):
        self.identifier = "rejectUser"
        self.label = "Reject User"
        self.fsm = fsm

    def onEnterState(self, counter):
        self.counter = counter

    def onExitState(self):
        pass

    def main(self):
        #display red cross
        self.log("Displaying red cross")
        time.sleep(5)
        #print("Counter is: ", self.counter)
        if self.counter == 1:
            self.log("Please measure your temperature again")
            self.fsm.transitionState("measureTemperature", self.counter)
        else:
            self.log("Temperature is too high please take a COVID test and isolate")
            # send alert to device owner
            self.fsm.transitionState("waitForHand")
