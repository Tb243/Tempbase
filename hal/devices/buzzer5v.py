from devices.device import Device
import RPi.GPIO as GPIO
import time

class buzzer5v(Device):

    def __init__(self):
        self.name = "BUZZER5V"
        self.isVirtual = False

    def validateConfig(self):
        return True
        
    def setup(self):
        GPIO.setup(self.buzzerPin, GPIO.OUT)

    def destroy(self):
        GPIO.cleanup()

    def read(self):
        pass

    def buzz(self):
        pwm = GPIO.PWM(self.buzzerPin, 50)
        pwm.start(0)
        pwm.ChangeDutyCycle(20.4)
        time.sleep(1)
        pwm.stop()

