from fsm.state import FsmState
import time

class StateProcessAndStoreTemp(FsmState):

    def __init__(self, fsm):
        self.identifier = "processAndStoreTemperature"
        self.label = "Process and store temperature"
        self.fsm = fsm

    def onEnterState(self, args):
        print("Entering the process and store temperature state")
        self.temperature = args[0]
        self.counter = args[1]
        
    def onExitState(self):
        print("Leaving process and store temperature state")

    def main(self):
        # add read (temp) value to database
        if self.temperature < 37.6:
            #display green tick
            print("Your temperature is: ", self.temperature)
            print("Green Tick being displayed")
            time.sleep(0.05)
            self.fsm.transitionState("displayQrCode")
        else : 
            print("Your temperature is: ", self.temperature)
            self.fsm.transitionState("rejectUser", self.counter)
        
  
         

        
