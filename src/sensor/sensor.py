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
status = 0

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
      with open("/home/pi/sensor/armed.txt", "r") as fo:
         fo.seek(0,0)
         status = fo.read(1)
      fo.closed
      
      if status == '1':
         date = datetime.datetime.today()
         img_name = date.strftime('%d-%m-%y-%H%M%S') + '.jpg'
         cam = subprocess.Popen("sudo fswebcam -r 320x240 -d /dev/video0 -q /home/pi/sensor/pics/" + img_name, shell=True)
         cam.wait()
         img_path = '/home/pi/sensor/pics/' + img_name
         upload = subprocess.Popen("sshpass -p 'bjm' scp " + img_path + " pi@192.168.1.150:/home/pi/MIDS", shell=True)
         upload.wait()
         time.sleep(2)
 
 	 # delete imag after sending
         subprocess.call("sudo rm " + img_path, shell=True)
      else:
	 print "    - Status: Unarmed."
 
   elif cur_pir==0 and prev_pir==1:
      # PIR returns to ready
      print "   Ready!"
      prev_pir = 0
   
   # sleep
   #time.sleep(0.5)
