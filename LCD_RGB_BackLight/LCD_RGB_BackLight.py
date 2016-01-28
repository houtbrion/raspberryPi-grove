
# Grovepi + grove RGB LCD module
 
# Example for using the Grove I2C color LCD
from grove_rgb_lcd import *

while(True):
    setText("Hello world\nLCD test")
    setRGB(0,128,64)
    for c in range(0,255):
        setRGB(c,255-c,0)
        time.sleep(0.01)
    setRGB(0,255,0)
    setText("Bye bye, this should wrap")
    time.sleep(1.5)

