import os
from twilio.rest import Client
from config import config

class SMSNotify:
    
    def __init__(self, system_number, account_sid, auth_token):
        self.name = "SMSNOTIFICATIONS"
        self.system_number = system_number
        self.account_sid = account_sid
        self.auth_token = auth_token
    
    
    def setup(self):
        pass
    
    def sendSMS(self, to, body):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
                        .create(
                            body=body,
                            from_=self.system_number,
                            to=to
                        )
    
    def smsTemp(self, recipient, temperature):
        numberTo = recipient
        numberFrom = config["twilio"]["numberFrom"]
        #numberTo = config["twilio"]["numberTo"]
        notifier = SMSNotify(numberFrom, config["twilio"]["accountSID"], config["twilio"]["authTok"])
        
        smsBody = "TempBase Alert: elevated temperature of " + str(temperature) + "detected."
       
        try:
           notifier.sendSMS(numberTo, smsBody )
           self.log("Success")
            
        except TwilioRestException as e:
            self.log("Unsuccessful")
          
        
    def smsRefill(self, recipient):
        numberTo = recipient  
        numberFrom = config["twilio"]["numberFrom"]
        #numberTo = config["twilio"]["numberTo"]
        notifier = SMSNotify(numberFrom, config["twilio"]["accountSID"], config["twilio"]["authTok"])
        
        try:
           notifier.sendSMS(numberTo, "TempBase Alert: Sanitiser is almost empty. Please refill")
           self.log("Success")
            
        except TwilioRestException as e:
            self.log("Unsuccessful")
    
    def smsCapacity(self, recipient):
        numberTo = recipient  
        numberFrom = config["twilio"]["numberFrom"]
        capacity = config["business"]["maxCapacity"]
        #numberTo = config["twilio"]["numberTo"]
        notifier = SMSNotify(numberFrom, config["twilio"]["accountSID"], config["twilio"]["authTok"])
        
        smsBody = "TempBase Alert: maximum capacity " + str(capacity) + "may be reached."

        try:
           notifier.sendSMS(numberTo, smsBody)
           self.log("Success")
            
        except TwilioRestException as e:
            self.log("Unsuccessful")     
        