from fsm import state_setup
from fsm import state_waitforhand
from fsm import state_dispensesanitiser
from fsm import state_measuretemperature
from fsm import state_processandstoretemp
from fsm import state_displayqrcode
from fsm import state_rejectuser

VIRTUAL_MODE = True
DEBUG_ON = True

class Fsm:

    def __init__(self):
        self.states = {}
        self.currentState = None

    def log(self, message):
        if DEBUG_ON:
            print("FSM: " + message)

    def addState(self, state):
        self.states[state.identifier] = state

    def transitionState(self, nextState, args=None):
        if not nextState in self.states:
            raise("Tried to transition to state '%s' which is an unknown state identifier" % nextState)

        if self.currentState and self.currentState in self.states:
            self.log("Calling onExitState for state '%s'" % self.currentState)
            self.states[self.currentState].onExitState()

        self.log("Setting state to '%s'" % nextState)
        self.currentState = nextState
        self.log("Calling onEnterState for state '%s'" % self.currentState)
        self.states[self.currentState].onEnterState(args)

    def spin(self):
        if not self.currentState:
            raise("FSM cannot spin without a current state")

        if not self.currentState in self.states:
            raise("Tried to spin in state '%s' which is an unknown state identifier" % self.currentState)

        self.log("Calling main for state '%s" % self.currentState)
        self.states[self.currentState].main()
        self.spin()

if __name__ == "__main__":
    fsm = Fsm()
    fsm.addState(state_setup.StateSetup(fsm))
    fsm.addState(state_waitforhand.StateWaitForHand(fsm))

    fsm.addState(state_setup.StateSetup(fsm))
    fsm.addState(state_dispensesanitiser.StateDispenseSanitiser(fsm))

    fsm.addState(state_setup.StateSetup(fsm))
    fsm.addState(state_measuretemperature.StateMeasureTemperature(fsm))
    
    fsm.addState(state_setup.StateSetup(fsm))
    fsm.addState(state_processandstoretemp.StateProcessAndStoreTemp(fsm))
 
    fsm.addState(state_setup.StateSetup(fsm))
    fsm.addState(state_displayqrcode.StateDisplayQrCode(fsm))
    
    fsm.addState(state_setup.StateSetup(fsm))
    fsm.addState(state_rejectuser.StateRejectUser(fsm))

    # Set initial state
    fsm.transitionState("setup")
    
    fsm.spin()