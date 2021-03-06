#!/usr/bin/python

import socket
import subprocess
from multiprocessing import Process
import time

class ClientProcess(Process):

    def __init__(self, ip, port, socket):
	Process.__init__(self)
        global start
	start = time.time()
	self.ip = ip
        self.port = port
        self.socket = socket
        print "  + New process started :- "+ip+":"+str(port)

    def run(self):
        
	try:
	    while True:
                data = self.socket.recv(1024)

                # if received 1, toggle arm/disarm
	    	if data=='1':
	    	    with open("/home/pi/sensor/armed.txt", "r+") as fo:
		        fo.seek(0,0)
		        state = fo.read(1)

			if state=='1':
		    	    state = '0'
		   	else:
		            state = '1'

			fo.seek(0,0)
			fo.write(state)
		    fo.closed	
         	   
		# if received 2, simulate preemption by flipping a byte 
		# to tell the sensor script not to capture any photo while,
                # preempt to the motion process to start streaming 
		elif data=='2':
		    with open("/home/pi/sensor/armed.txt", "r+") as fo:
			fo.seek(0,0)
			state = fo.read(1)

			# set to disarmed to be able to use the videocam source
			if state=='1':
			    fo.seek(0,0)
			    state = '0'
			    fo.write(state)
		    fo.closed

		    # now, start the motion process to livestream
		    subprocess.call("sudo motion", shell=True)

		# 3, to pause the motion process and continue sensor process
		elif data=='3':
		    with open("/home/pi/sensor/armed.txt", "r+") as fo:
			fo.seek(0,0)
			state = fo.read(1)

			# set to arm the sensor
			if state=='0':
			    fo.seek(0,0)
			    state = '1'
			    fo.write(state)
		    fo.closed

		    # get the pid of motion
		    with open("/home/pi/motion/motion.pid", "r") as fo:
			line = fo.readline()
		    fo.closed

		    # now, kill the motion process to continue sensor process
		    subprocess.call("sudo kill "+line, shell=True)

		self.socket.send(state)

	except:
            print "Lost connection to client..."
        finally:
            print "Client disconnected..."
	    print "Total Execution Time: ", (time.time() - start)
            self.socket.close()
	    
host = "0.0.0.0"
port = 42500

servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

servsock.bind((host,port))
process = []


while True:
    servsock.listen(5)
    print "\nListening for incoming connections..."
    (clientsock, (ip, port)) = servsock.accept()
    newProcess = ClientProcess(ip, port, clientsock)
    newProcess.start()
    process.append(newProcess)

for p in process:
    p.join()
        
