
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import config


class Notifications:
    
    
    def __init__(self, system_email, system_pass):
        self.name = "NOTIFICATIONS"
        self.system_email = system_email
        self.system_pass = system_pass
        
    def setup():
        pass

    def sendEmail(self, receipient, subject, body):
            # Send email
            MESSAGE = MIMEMultipart('alternative')
            MESSAGE['subject'] = subject
            MESSAGE['To'] = receipient
            MESSAGE['From'] = self.system_email
            # Add body to email
            HTML_EMAIL_BODY = MIMEText(body, 'html')
            MESSAGE.attach(HTML_EMAIL_BODY)
            # Send

            # TODO: Change the server parameters to use the config file.
            mail = smtplib.SMTP(config["transport"]["smtpServer"], config["transport"]["smtpPort"])

            mail.ehlo()
            mail.starttls()
            mail.login(self.system_email, self.system_pass)
            mail.sendmail("AAIMI", receipient, MESSAGE.as_string())
            mail.close()
            print("Message sent")

    def sendTemp(self, recipient, temperature):
        emailBody = """
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
            <p>The temperature is 
        """

        emailBody += str(temperature) + "</p></body>"

        self.sendEmail(recipient, "Temperature alert", emailBody)

    def sendRefill(self, recipient):
        emailBody = """
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>The bottle is empty</title>
        <style type="text/css" media="screen">
            h1{ color:white;font-size:2.5em;background-color:red;text-align:center;}
            h2{color:gray;font-size:2em;text-align:center;}
            h3{color:purple;font-size:2em;text-align:center;}
            p{color:blue;font-size:1.5em;text-align:center;}
        </style>
        </head>
        <body>
        <p>The bottle needs to be refilled</p>
        </body>
        """

        self.sendEmail(recipient, "Refill alert", emailBody)
               
                


