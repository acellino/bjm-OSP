#!/usr/bin/python

import sys

#----- Main -----     
timestamp = sys.argv[1]     
 
with open("/home/pi/sensor/test/pir_result2.txt", "w") as fo:
   fo.seek(0,0)
   fo.write(timestamp)
fo.closed
 
