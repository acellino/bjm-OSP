#!/usr/bin/python

import datetime

#----- Main -----     
date = datetime.datetime.today()
timestamp  = date.strftime('%d-%m-%y-%H:%M:%S')
      
with open("/home/pi/sensor/test/pir_result1.txt", "w") as fo:
   fo.seek(0,0)
   fo.write(timestamp)
fo.closed
 
