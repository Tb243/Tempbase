import board
import adafruit_mlx90614
import RPi.GPIO as GPIO
import time

class Thermometer:
	def __init__(self):
		self.i2c = board.I2C()
		self.thermo = adafruit_mlx90614.MLX90614(self.i2c)

	def ambient_temperature(self):
		return self.mlx.ambient_temperature

	def object_temperature(self):
		return self.mlx.object_temperature
