from states import state

class StateDispenseSanitiser(state.FsmState):

    def __init__(self, fsm):
        self.identifier = "dispenseSanitiser"
        self.label = "Dispense Sanitiser"
        self.fsm = fsm

    def onEnterState(self, counter):
        print("Entering the dispense sanitiser state")
        # src04.setup()
        self.counter = counter

    def onExitState(self):
        print("Leaving the dispense sanitiser state")
        # Check if sanitiser level is empty
        # If it is, send an alert to the device owner.

    def main(self):
        while True:
            # turn = fs90r.turn()
            turn = float(input("Enter 0 for sanitiser to dispense: "))
            if turn < 1:
                break

        self.fsm.transitionState("measureTemperature", self.counter)
