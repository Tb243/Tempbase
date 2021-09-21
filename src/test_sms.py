from notifications.notify_sms import SMSNotify
from config import config

notifier = SMSNotify(config["twilio"]["systemNumber"], config["twilio"]["accountSID"], config["twilio"]["authTok"])
for recipient in config["twilio"]["numberTo"]:
    notifier.smsTemp(recipient, 38.1)
    notifier.smsRefill(recipient)