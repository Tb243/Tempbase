import board
import adafruit_mlx90614
import RPi.GPIO as GPIO
import time


i2c = board.I2C()
mlx = adafruit_mlx90614.MLX90614(i2c)

servo = 12
buzzer = 26
led = 19
trig = 6
echo = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, 0)
print("calibrating sensor")
time.sleep(2)
GPIO.output(trig, 1)
time.sleep(0.00001)
GPIO.output(trig, 0)

while GPIO.input(echo) == 0:
    pulse_start = time.time()
    
while GPIO.input(echo) == 1:
    pulse_end = time.time()
    
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)
print("Distance: ", distance, "cm")

pwm = GPIO.PWM(servo, 50)
pwm.start(0)
try:
    pwm.ChangeDutyCycle(20.4)
    print("Ambient Temp: ", mlx.ambient_temperature)
    print("Object Temp: ", mlx.object_temperature)
    time.sleep(1)
    pwm.stop()
    GPIO.output(buzzer, 1)
    GPIO.output(led, 1)
    time.sleep(0.5)
    GPIO.output(buzzer, 0)
    GPIO.output(led, 0)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

