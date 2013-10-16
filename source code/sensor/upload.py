#!/usr/bin/python
#upload.py

import sys
import subprocess
import time

filepath = sys.argv[1]

subprocess.call("sshpass -p 'bjm' scp " + filepath + " pi@192.168.1.150:/home/pi/MIDS",shell=True)

time.sleep(10)

subprocess.call("sudo rm " + filepath, shell=True)

