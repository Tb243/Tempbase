import board
import RPi.GPIO as GPIO
import time


levin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(levin, GPIO.IN)

def main():
    while True:
        try:
            print(GPIO.input(levin))
            time.sleep(1)
        except KeyboardInterrupt:
            GPIO.cleanup()

if __name__=="__main__":
    main()

