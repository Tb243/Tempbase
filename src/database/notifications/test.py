from notify import Notifications
import getpass
import time

class testNotifications:
    
    def testEmail():
        
        
        #get password for sending email pw = sit312project
        print("Enter password for " + Notifications.system_email)
        pw = str(getpass.getpass())
        Notifications.system_pass = pw
        
        #time limit for subsequent emails
        time_limit = 30
        last_email = time.time() - time_limit   
        
        temperature = 38.9
        
        try:
            
            if (time.time() - last_email) > time_limit:
                last_email = time.time()
                Notifications.send_email_report("Elevated temperature recorded ", time.strftime("%d:%h:%m"), temperature)
                print('success')
        except:
            print("email notification unsuccessful")
            
    def testSms():
        pass
