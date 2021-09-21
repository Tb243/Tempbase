from notifications.notify import Notifications
import getpass
import time
from config import config

print("Send to whom?")
receipient = str(input())
notifier = Notifications(config["email"]["transport"]["username"], config["email"]["transport"]["password"])

temperature = str(38.9)
notifier.sendTemp(receipient, temperature)
notifier.sendRefill(receipient)