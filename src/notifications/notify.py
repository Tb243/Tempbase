
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Notifications:
    
    
    def __init__(self, system_email, system_pass, user_email):
        self.name = "NOTIFICATIONS"
        self.system_email = system_email
        self.system_pass = system_pass
        self.user_email = user_email
        
    def setup():
        pass
        
    # Send email alerts to users. Requires dedicated Gmail account for AAIMI      
    def email_notify(self, sub, arg1, arg2, arg3=""):
        
        
        if self.system_pass != "":    
            # Create HTML head for email 
            head = """
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>TempBase Alert</title>
            <style type="text/css" media="screen">
                h1{ color:white;font-size:2.5em;background-color:red;text-align:center;}
                h2{color:gray;font-size:2em;text-align:center;}
                h3{color:purple;font-size:2em;text-align:center;}
                p{color:blue;font-size:1.5em;text-align:center;}
            </style>
            </head>
            <body>
            """

            # Create HTML for body with subject and args
            message_body = "<h1>" + sub + "</h1><p>" + arg1 + "</p><p>" + arg2 + "</p>"
            if arg3 != "":
                message_body += "<p>" + arg3 + "</p>"            
            message_body += "</body>"        
            full_email = head + message_body

            # Send email
            MESSAGE = MIMEMultipart('alternative')
            # Email details
            MESSAGE['subject'] = sub
            MESSAGE['To'] = self.user_email
            MESSAGE['From'] = self.system_email
            # Add body to email
            HTML_EMAIL_BODY = MIMEText(full_email, 'html')
            MESSAGE.attach(HTML_EMAIL_BODY)
            # Send
            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.system_email, self.system_pass)
            mail.sendmail("AAIMI", self.user_email, MESSAGE.as_string())
            mail.close()
            print("Message sent")
                
                
    def sms_notify():
        pass


