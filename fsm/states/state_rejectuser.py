from states import state
import time

class StateRejectUser(state.FsmState):

    def __init__(self, fsm):
        self.identifier = "rejectUser"
        self.label = "Reject User"
        self.fsm = fsm

    def onEnterState(self, counter):
        print("Entering the reject user state")
        self.counter = counter

    def onExitState(self):
        print("Leaving the reject user state")

    def main(self):
        #display red cross
        print("Displaying red cross")
        time.sleep(5)
        #print("Counter is: ", self.counter)
        if self.counter == 1:
            print("Please measure your temperature again")
            self.fsm.transitionState("measureTemperature", self.counter)
        else:
            print("Temperature is too high please take a COVID test and isolate")
            # send alert to device owner
            self.fsm.transitionState("waitForHand")
