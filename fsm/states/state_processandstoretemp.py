from states import state
import time

class StateProcessAndStoreTemp(state.FsmState):

    def __init__(self, fsm):
        self.identifier = "processAndStoreTemperature"
        self.label = "Process and store temperature"
        self.fsm = fsm

    def onEnterState(self, temperature):
        print("Entering the process and store temperature state")
        self.temperature = temperature
        

    def onExitState(self):
        print("Leaving process and store temperature state")

    def main(self):
        # add read (temp) value to database
        if self.temperature < 37.6:
            #display green tick
            print("Green Tick being displayed")
            time.sleep(0.05)
            self.fsm.transitionState("displayQrCode")
        else : 
            self.fsm.transitionState("rejectUser")
        
  
         

        
