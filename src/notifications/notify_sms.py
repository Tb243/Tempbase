import os
from twilio.rest import Client

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

        #print(message.sid)      