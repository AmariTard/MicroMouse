from microbit import *
import neopixel
from random import randint
import time

#RGB

np = neopixel.NeoPixel(pin0, 16)
locked = False
happy = False


while True:

    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)

        np[pixel_id] = (red, green, blue)

        np.show()
        #sleep(100)


    if (button_a.is_pressed() or not pin1.read_digital()):
        if (locked == False):
            locked = True
            happy = not happy
            if (happy == True):
                print('1')
                # display.show(Image.HAPPY)
                display.set_pixel(0,0,9)
            else:
                # display.show(Image.SAD)
                print('0')
                display.set_pixel(0,0,0)
            time.sleep_ms(10)
                
    else:
        locked = False
