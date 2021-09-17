from notify import Notifications
import getpass
import time

class testNotifications:
    
    def testEmail(self):
        
        
        #get password for sending email pw = xxxxxxxx
        email = "tempbasenotifications@gmail.com"
        print("Enter password for " + email)
        pw = str(getpass.getpass())
        notifier = Notifications(email, pw, "tempbasenotifications@gmail.com")
        
        #time limit for subsequent emails
        time_limit = 30
        last_email = time.time() - time_limit   
        
        temperature = str(38.9)
        
        if (time.time() - last_email) > time_limit:
            last_email = time.time()
            notifier.email_notify("Elevated temperature recorded ", time.strftime("%d:%h:%m"), temperature)
            print('success')
            
    def testSms(self):
        pass

if __name__ == "__main__":
    test = testNotifications()
    test.testEmail()