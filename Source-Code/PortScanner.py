import socket
import subprocess
import sys
from datetime import datetime

#Clear the screen
subprocess.call('cls', shell=True)

#Ask for input
remoteServer = input("Enter host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("Scanning remote host", remoteServerIP)

#Check what time the scan started
t1 = datetime.now()

try:
    for port in range(11025):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:   Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Ctrl+C pressed")
    sys.exit()

except socket.error:
    print("Connection error")
    sys.exit()

#Checking time again
t2 = datetime.now()

#calculate total time
total = t2-t1

print("Scanning Completed in: ", total)
