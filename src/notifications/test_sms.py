from notify_sms import SMSNotify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


class testSMSNotifications:
    
    def testSMS(self):
        
        numberTo = "+61400000000"
        numberFrom = "+61400000001"
        notifier = SMSNotify(numberFrom, numberTo)
        
        try:
        # This could potentially throw an exception!
           notifier.sendSMS()
            
        except TwilioRestException as e:
            # Implement your fallback code
            print(e)
            
 
if __name__ == "__main__":
        test = testSMSNotifications()
        test.testSMS()   