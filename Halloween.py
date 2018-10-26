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
    for channel in range(4):
        chasingPixels = [-2,-1,0]
        for pixel in range(mote.get_pixel_count(channel + 1)):
            r, g, b = colorsToPop[channel]
            for(i, chasingPixel) in enumerate(chasingPixels):
                if (chasingPixel >= 0 and chasingPixel <= 16):
                    mote.set_pixel(channel + lightdirection, chasingPixel, r, g, b)
                    mote.show()
#                    time.sleep(0.02)
                chasingPixels[i] = chasingPixel + 1
            
                #will this turn off the pixels?
                if (lightdirection < 0):
                    lastPixelToRemove = min(chasingPixels)
                else:
                    lastPixelToRemove = max(chasingPixels)

                if (lastPixelToRemove > 0 and lastPixelToRemove <= 16):
                    for pixelToTurnOff in range(lastPixelToRemove - 1):
                        mote.set_pixel(channel + 1, pixelToTurnOff, 0, 0, 0)
            mote.show()
            time.sleep(0.02)
                
            if (lastPixelToRemove == 16):
                for pixel in range(mote.get_pixel_count(channel + 1)):
                        mote.set_pixel(channel + 1, pixel, r, g, b)
                        mote.show()
                        time.sleep(0.02)
        colorsToPop.append(colorsToPop.pop(0))

while True:
    colorsToPop = colors    
    # # Display solid colour test
    # for step in range(4):
    #     for channel in range(4):
    #         for pixel in range(mote.get_pixel_count(channel + 1)):
    #             r, g, b = colorsToPop[channel]
    #             mote.set_pixel(channel + 1, pixel, r, g, b)
    #             mote.show()
    #             time.sleep(0.01)

    #     colorsToPop.append(colorsToPop.pop(0))

    knightRider(1)
    knightRider(-1)

    # Display solid colour test


        