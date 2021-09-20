from notifications.notify_sms import SMSNotify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from config import config

class testSMSNotifications:
    
    def testSMS(self):
        
        numberTo = "+61411166441"
        numberFrom = "+61488882708cd"
        notifier = SMSNotify(numberFrom, config["twilio"]["accountSID"], config["twilio"]["authTok"])
        
        try:
        # This could potentially throw an exception!
           notifier.sendSMS(numberTo, "This is a test message")
            
        except TwilioRestException as e:
            # Implement your fallback code
            print(e)
            
 
if __name__ == "__main__":
        test = testSMSNotifications()
        test.testSMS()   