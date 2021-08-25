import time
from hardware import thermometer

thermo = thermometer.Thermometer()

while True:
	print("Ambient temperature: %f, object temperature: %f" % (thermo.ambient_temperature(), thermo.object_temperature()))
	time.sleep(0.5)