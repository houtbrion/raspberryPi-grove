import grove_compass_lib
import time
c=grove_compass_lib.compass()
while True:
        print "X:",c.x,"Y:",c.y,"X:",c.z,"Heading:",c.headingDegrees
        c.update()
        time.sleep(.1)
