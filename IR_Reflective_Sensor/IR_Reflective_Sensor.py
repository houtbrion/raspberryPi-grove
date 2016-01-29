import time
import grovepi



# Connect the Grove Infrared Reflective Sensor to digital port D4
# SIG,NC,VCC,GND
sensor = 4

grovepi.pinMode(sensor,"INPUT")

while True:
    try:
        # Sensor returns HIGH on a black surface and LOW on a white surface
        if grovepi.digitalRead(sensor) == 1:
            print "black surface detected"
        else:
            print "white surface detected"

        time.sleep(.5)

    except IOError:
        print "Error"

