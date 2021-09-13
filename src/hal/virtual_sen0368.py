from hal.device import Device
import time
import random

class VirtualSEN0368(Device):

    def __init__(self, liquidPin=None):
        self.name = "Virtual SEN0368"
        self.isVirtual = True
        self.liquidPin = liquidPin

    def validateConfig(self):
        return True 


    def setup(self):
        time.sleep(2.0)

    def destroy(self):
        pass

    def read(self):
        time.sleep(0.00001)
        return round(random.uniform(0, 1))
