# The MIT License (MIT)
#
# Copyright (c) 2017 Dan Halbert for Adafruit Industries
# Copyright (c) 2017 Kattni Rembor, Tony DiCola for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Modified by Robert Babb for OSMM Intro to Python Class

import array
import math
import time
import audiobusio
import board
import neopixel

# Exponential scaling factor.
# Should probably be in range -10 .. 10 to be reasonable.
CURVE = 2
SCALE_EXPONENT = math.pow(10, CURVE * -0.1)

NUM_PIXELS = 10

# Number of samples to read at once.
NUM_SAMPLES = 160

def mean(values):
    return sum(values) / len(values)

# Remove DC bias before computing RMS.
def normalized_rms(values):
    minbuf = int(mean(values))
    
    # remove DC bias and square samples
    samples = []
    for sample in values:
        samples.append(float(sample - minbuf) * (sample - minbuf))
        
    samples_sum = sum(samples)
    return math.sqrt(samples_sum / len(values))

# Scale input_value between output_min and output_max, exponentially.
def log_scale(input_value, input_min, input_max, output_min, output_max):
    normalized_input_value = (input_value - input_min) / \
                             (input_max - input_min)
    return output_min + \
        math.pow(normalized_input_value, SCALE_EXPONENT) \
        * (output_max - output_min)

# Restrict value to be between floor and ceiling.
def constrain(value, floor, ceiling):
    return max(floor, min(value, ceiling))

def bgr_vol_2_color(val):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition b - g - r.
        
    # Make sure val is in range
    val = constrain(val, 0, 255)
    if val == 0:
        return (0, 0, 0)
        
    if val < 127:
        return (0, int(val * 2), int(255 - val * 2))
    else:
        val -= 127
        return (int(val * 2), int(255 - (val * 2)), 0)         

def do_lvl_3_color_meter(snd_level, pixels):
    # Light up pixels that are below the scaled and interpolated magnitude.
    pixels.fill(bgr_vol_2_color(snd_level))
    pixels.show() 
    
def main():

    pixels = neopixel.NeoPixel(board.NEOPIXEL, NUM_PIXELS,
                               brightness=0.1, auto_write=False)
    pixels.fill((100, 0, 100))
    pixels.show() 
    time.sleep(2)

    # For Circuitpython 3.0 and up, "frequency" is now called "sample_rate".
    # Comment the lines above and uncomment the lines below.
    mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                           sample_rate=16000, bit_depth=16)

    # Record an initial sample to calibrate. Assume it's quiet when we start.
    samples = array.array('H', [0] * NUM_SAMPLES)
    mic.record(samples, len(samples))
    # Set lowest level to expect, plus a little.
    input_floor = normalized_rms(samples) + 20
    # OR: used a fixed floor
    # input_floor = 50
    # You might want to print the input_floor to help adjust other values.
    # print(input_floor)
    # Corresponds to sensitivity: 
    #     lower means more pixels light up with lower sound
    # Adjust this as you see fit.
    input_ceiling = input_floor + 500    
    
    while True:
        mic.record(samples, len(samples))
        magnitude = normalized_rms(samples)
        # You might want to print this to see the values.
        # print(magnitude)

        # Compute scaled logarithmic reading in the range 0 to number of colors
        c = log_scale(constrain(magnitude, input_floor, input_ceiling),
                      input_floor, input_ceiling, 0, 255)
        
        # Filter out noise, brute force, can be improved
        if c < 50:
            c = 0
            
        do_lvl_3_color_meter(c, pixels)

if __name__ == '__main__':
    main()
