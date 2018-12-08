from machine import Pin


class MS:
    def __init__(self, pin):
        self.pin = pin

    def check(self):
        return Pin(self.pin, Pin.IN).value()
