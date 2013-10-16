#!/usr/bin/python

import sys
import socket
import time

def main(args):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        host = "192.168.1.150"
        port = 42500
        client.connect((host, port))
        client.sendall(args)
        state = client.recv(1024)
        
	# receive the current state of arm/disarm of sensor
	# and write to armed.txt
        with open ("/home/pi/armed.txt", "w") as fo:
            fo.seek(0,0)
	    fo.write(state)
	fo.closed
	
	time.sleep(0.5)
	client.close()
    except Exception as msg:
        print msg

if __name__ == "__main__":
    main(sys.argv[1])
