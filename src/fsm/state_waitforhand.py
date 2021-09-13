from fsm.state import FsmState

class StateWaitForHand(FsmState):

    def __init__(self, fsm):
        self.identifier = "waitForHand"
        self.label = "Wait for hand"
        self.fsm = fsm

    def onEnterState(self, args=None):
        print("Entering the wait for hand state")
        # src04.setup()
        

    def onExitState(self):
        print("Leaving the wait for hand state")

    def main(self):
        counter = 0
        #print("Counter is: ", counter)
        while True:
            # distance = src04.read()
            distance = float(input("Enter distance: "))
            if distance < 10:
                break

        self.fsm.transitionState("dispenseSanitiser", counter)
