#!/usr/bin/python

import subprocess
import RPi.GPIO as io
import time
import datetime

io.setmode(io.BCM)

pir_pin = 7

io.setup(pir_pin, io.IN)

#----- Main -----
cur_pir = 0
prev_pir = 0

print "Waiting for PIR to settle.."

while io.input(pir_pin)==1:
  cur_pir=0

print "   READY"

# Starts capturing signal
while True :

   # Read PIR state
   cur_pir = io.input(pir_pin)

   if cur_pir==1 and prev_pir==0:
      # PIR is triggered
      print "   Motion detected!"
      prev_pir=1
     
      date = datetime.datetime.today()
      timestamp  = date.strftime('%d-%m-%y-%H:%M:%S')
      
      with open("/home/pi/sensor/test/pir_result.txt", "w") as fo:
         fo.seek(0,0)
         fo.write(timestamp)
      fo.closed
 
   elif cur_pir==0 and prev_pir==1:
      # PIR returns to ready
      print "   Ready!"
      prev_pir = 0
   
   # sleep
   #time.sleep(0.5)
