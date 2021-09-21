import os
from fsm.state import FsmState
import time
from notifications.notify import Notifications
from notifications.notify_sms import SMSNotify
from config import config

VIRTUAL_MODE = True if os.environ.get("virtualMode") == "on" else False

if VIRTUAL_MODE:
    from hal.virtual_buzzer5v import VirtualBUZZER5V as Buzzer5v
else:
    from hal.buzzer5v import Buzzer5v

class StateRejectUser(FsmState):

    def __init__(self, fsm):
        self.identifier = "rejectUser"
        self.label = "Reject User"
        self.fsm = fsm
        self.buzzer = Buzzer5v(26)
        
    def onEnterState(self, args):
        self.temperature = args[0]
        self.counter = args[1]
        self.buzzer.setup()

    def onExitState(self):
        pass

    def main(self):
        #display red cross
        self.log("Displaying red cross")
        time.sleep(5)
        if self.counter == 1:
            self.buzzer.buzz(0.5)
            self.log("BUZZ")
            self.log("Please measure your temperature again")
            time.sleep(2)
            self.fsm.transitionState("measureTemperature", self.counter)
        else:
            self.log("Temperature is too high please take a COVID test and isolate")
            self.buzzer.buzz(0.5)
            self.log("BUZZ")
            time.sleep(2)
            self.sendAlert(self.temperature, 1, 1)
            self.fsm.transitionState("waitForHand")
            
        # Send the alert to the device owner - 1 for yes, 0 for no
    def sendAlert(self, temp, sms, email):
        self.temperature = temp
        smsAlert = sms
        emailAlert = email

        try:
            if smsAlert == 1:
                for recipient in config["twilio"]["numberTo"]:
                    SMSNotify.smsTemp(recipient, self.temperature)
                self.log("Santise SMS success")
            else:
                pass
            
            if emailAlert == 1:
                for recipient in config["email"]["recipients"]:
                    Notifications.sendTemp(recipient, self.temperature)
                self.log("Sanitise email success")
            else:
                pass
        except:
            self.log("Unsuccesful")
