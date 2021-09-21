import os
from twilio.rest import Client
from config import config

class SMSNotify:
    
    def __init__(self, system_number, account_sid, auth_token):
        self.system_number = system_number
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(self.account_sid, self.auth_token)
    
    def sendSMS(self, to, body):
        self.client.messages \
                        .create(
                            body=body,
                            from_=self.system_number,
                            to=to
                        )
    
    def smsTemp(self, recipient, temperature):
        smsBody = "TempBase Alert: elevated temperature of " + str(temperature) + " detected."
        self.sendSMS(recipient, smsBody)
          
    def smsRefill(self, recipient):
        self.sendSMS(recipient, "TempBase Alert: Sanitiser is almost empty. Please refill")
    
    def smsCapacity(self, recipient, capacity):
        smsBody = "TempBase Alert: maximum capacity " + str(capacity) + " may be reached."
        self.sendSMS(recipient, smsBody)
        