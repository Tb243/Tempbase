from hal.device import Device
import board
import adafruit_mlx90614

class MLX90614(Device):

	def __init__(self):
		self.name = "MLX90614"
		self.isVirtual = False

	def validateConfig(self):
		return True

	def setup(self):
		self.i2c = board.I2C()
		self.mlx = adafruit_mlx90614.MLX90614(self.i2c)

	def destroy(self):
		pass

	def read(self):
		return self.mlx.object_temperature
