from devices import virtual_hcsr04

device = virtual_hcsr04.VirtualHCSR04()
print("Setting up device...")
device.setup()
print("Reading distance...")
distance = round(device.read(), 2)
print("The distance is approximately %sCM" % distance)
device.destroy()