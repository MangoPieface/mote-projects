import time
from colorsys import hsv_to_rgb, rgb_to_hsv
from mote import Mote
from flask import Flask, jsonify, make_response

app = Flask(__name__)
mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

colour = 'B8995F'
status = 0
num_pixels = 16
num_channels = 4

def hex_to_rgb(value):
    value = value.lstrip('#')
    length = len(value)
    return tuple(int(value[i:i + length / 3], 16) for i in range(0, length, length / 3))

def mote_on(c):
    global num_pixels
    global num_channels
    r, g, b = hex_to_rgb(c)
    testforwhite = c.lstrip('#')
    if  testforwhite == 'FFFFFF':
	    exec(open("./rainbow.py"))
    else:
    	for channel in range(num_channels):
        	for pixel in range(num_pixels):
            		mote.set_pixel(channel + 1, pixel, 255, 228, 225)
    			mote.show()
    return True

def mote_off():
    mote.clear()
    mote.show()
    return True

def get_status():
    global status
    global num_channels
    global num_pixels

    for channel in range(num_channels):
        for pixel in range(num_pixels):
            if mote.get_pixel(channel + 1, pixel) != (0, 0, 0):
                status = 1
            else:
                status = 0
    return status

@app.route('/mote/api/v1.0/<string:st>', methods=['GET'])
def set_status(st):
    global status, colour, num_channels, num_pixels
    if st == 'on':
        status = 1
        mote_on(colour)
        brightness = 0
        for h in range(1000):
            for channel in range(num_channels):
                for pixel in range(mote.get_pixel_count(channel + 1)):
                    hue = (h + (channel * num_pixels * 4) + (pixel * 4)) % 360
                    r, g, b = [int(c * brightness) for c in hsv_to_rgb(hue/360.0, 1.0, 1.0)]
                    mote.set_pixel(channel + 1, pixel, r, g, b)
            mote.show()
            time.sleep(0.01)
            if brightness < 255: brightness += 1        
    elif st == 'off':
        status = 0
        mote_off()
    elif st == 'status':
        status = get_status()
    return jsonify({'status': status, 'colour': colour})

@app.route('/mote/api/v1.0/set', methods=['GET'])
def get_colour():
    global colour
    return jsonify({'status': status, 'colour': colour})

@app.route('/mote/api/v1.0/set/<string:c>', methods=['GET'])
def set_colour(c):
    global status, colour
    colour = c
    if status != 0:
        mote_on(colour)
        status = 1
    return jsonify({'status': status, 'colour': colour})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    mote_off()
    app.run(host='0.0.0.0', debug=True)
