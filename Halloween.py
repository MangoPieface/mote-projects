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

    # Display solid colour test
    for step in range(4):
        for channel in range(4):
            chasingPixels = [0,1,2]
            for pixel in range(mote.get_pixel_count(channel + 1)):
                r, g, b = colorsToPop[channel]
                for(i, chasingPixel) in enumerate(chasingPixels):
                    if (chasingPixel >= 0 and chasingPixel < 16):
                        mote.set_pixel(channel + 1, chasingPixel, r, g, b)
                        mote.show()
                        time.sleep(0.1)
                    chasingPixels[i] = chasingPixel + 1
                
                    #will this turn off the pixels?
                    lastPixelToRemove = min(chasingPixels)
                    if (lastPixelToRemove >= 0 and lastPixelToRemove < 16):
                        for pixelToTurnOff in range(lastPixelToRemove):
                            mote.set_pixel(channel + 1, pixelToTurnOff, 0, 0, 0)
                            mote.show()

        colorsToPop.append(colorsToPop.pop(0))