#!/usr/bin/env python

import time
from colorsys import hsv_to_rgb

from mote import Mote


mote = Mote()

num_pixels = 16

mote.configure_channel(1, num_pixels, False)
mote.configure_channel(2, num_pixels, False)
mote.configure_channel(3, num_pixels, False)
mote.configure_channel(4, num_pixels, False)

colors = [
    (255,   0,   0),
    (0,   255,   0),
    (255,   0,   0),
    (0,   255,   0)
]    



def knightRider(lightdirection):
    timer = .001
    
    for pixel in range(15):
        for channel in range(4):
            r, g, b = colorsToPop[channel]
            mote.set_pixel(channel + 1, pixel, r, g, b)
            mote.show()
            #time.sleep(timer)
            mote.set_pixel(channel + 1, pixel + 1, r, g, b)
            mote.show()
            #time.sleep(timer)
            mote.set_pixel(channel + 1, pixel, 0, 0, 0)
            mote.show()
            time.sleep(timer * 2)
    
    for pixel in range(15, 0, -1):
        for channel in range(4):
            r, g, b = colorsToPop[channel]
            mote.set_pixel(channel + 1, pixel, r, g, b)
            mote.show()
            #time.sleep(timer)
            mote.set_pixel(channel + 1, pixel - 1, r, g, b)
            mote.show()
            #time.sleep(timer)
            mote.set_pixel(channel + 1, pixel, 0, 0, 0)
            mote.show()
            time.sleep(timer * 2)
        colorsToPop.append(colorsToPop.pop(0))

while True:
    colorsToPop = colors    
    knightRider(1)
    #knightRider(-1)

    # Display solid colour test


        