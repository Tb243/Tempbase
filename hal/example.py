from devices import virtual_hcsr04
from devices import virtual_mlx90614

device = virtual_hcsr04.VirtualHCSR04()
print("Setting up device...")
device.setup()
print("Reading distance...")
distance = round(device.read(), 2)
print("The distance is approximately %sCM" % distance)
device.destroy()

temperature_device = virtual_mlx90614.VirtualMLX90614()
temperature_device.setup()
print("The temperature is %s" % temperature_device.read())