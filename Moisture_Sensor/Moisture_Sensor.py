import time
import grovepi
 
# Connect the Grove Moisture Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 0
 
while True:
    try:
        print grovepi.analogRead(sensor)
        time.sleep(.5)
 
    except KeyboardInterrupt:
        break
    except IOError:
        print "Error"

