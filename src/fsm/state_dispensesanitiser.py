from fsm.state import FsmState
from hal import virtual_hcsr04

class StateDispenseSanitiser(FsmState):

    def __init__(self, fsm):
        self.identifier = "dispenseSanitiser"
        self.label = "Dispense Sanitiser"
        self.fsm = fsm

    def onEnterState(self, counter):
        # src04.setup()
        self.counter = counter

    def onExitState(self):
        pass
        # Check if sanitiser level is empty
        # If it is, send an alert to the device owner.

    def main(self):
        while True:
            # turn = fs90r.turn()
            turn = float(input("Enter 0 for sanitiser to dispense: "))
            if turn < 1:
                break

        self.fsm.transitionState("measureTemperature", self.counter)
