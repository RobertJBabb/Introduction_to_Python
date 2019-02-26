# CircuitPlaygroundExpress_NeoPixel

import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

def simpleCircle(wait):
    RED = 0x100000  # (0x10, 0, 0) also works
    YELLOW = (0x10, 0x10, 0)
    GREEN = (0, 0x10, 0)
    AQUA = (0, 0x10, 0x10)
    BLUE = (0, 0, 0x10)
    PURPLE = (0x10, 0, 0x10)
    BLACK = (0, 0, 0)

    for i in range(len(pixels)):
        pixels[i] = RED
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = YELLOW
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = GREEN
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = AQUA
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLUE
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = PURPLE
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLACK
        time.sleep(wait)
    time.sleep(1)


while True:
    print('Neopixel Demo')
    simpleCircle(.05)

