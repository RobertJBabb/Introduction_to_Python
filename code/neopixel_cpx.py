import time

from adafruit_circuitplayground.express import cpx

RED = (10, 0, 0)
YELLOW = (10, 10, 0)
GREEN = (0, 10, 0)
AQUA = (0, 10, 10)
BLUE = (0, 0, 10)
PURPLE = (10, 0, 10)
BLACK = (0, 0, 0)

while True:
    print("Neopixel CPX lib Demo")
    cpx.pixels.brightness = 0.2

    print('Simple Circle Demo')
    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = RED
        time.sleep(.05)
    time.sleep(1)

    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = YELLOW
        time.sleep(.05)
    time.sleep(1)

    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = GREEN
        time.sleep(.05)
    time.sleep(1)

    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = AQUA
        time.sleep(.05)
    time.sleep(1)

    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = BLUE
        time.sleep(.05)
    time.sleep(1)

    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = PURPLE
        time.sleep(.05)
    time.sleep(1)

    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = BLACK
        time.sleep(.05)
    time.sleep(1)


