import os
from twilio.rest import Client

class SMSNotify:
    
    def __init__(self, system_number, user_number):
        self.name = "SMSNOTIFICATIONS"
        self.system_number = system_number
        self.user_email = user_number
    
    
    def setup():
        pass
    
    def sendSMS():
        
        account_sid = os.environ['AC4125a91837bcfebf3c6e2c19644eb2de']
        auth_token = os.environ['20c17f516cc513be6cccb6d734689541'] 
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                            from_='+15017122661',
                            to='+15558675310'
                        )

        #print(message.sid)      