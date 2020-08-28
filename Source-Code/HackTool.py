import socket
import subprocess
import sys
from datetime import datetime

def port_scanner():
    # Clear the screen
    subprocess.call('cls', shell=True)

    # Ask for input
    remoteServer = input("Enter host to scan: ")
    socketRange = int(input("Enter range of port: "))
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("Scanning remote host", remoteServerIP)

    # Check what time the scan started
    t1 = datetime.now()

    try:
        for port in range(socketRange):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creates a stream socket
            # SOCK_STREAM 为Socket type TCP connections
            result = sock.connect_ex(
                (remoteServerIP, port))  # sock.connect_ex((remoteServerIP, port)) return 0 if success
            if result == 0:
                print("Port {}:   Open".format(port))
        sock.close()

    except KeyboardInterrupt:
        print("Ctrl+C pressed")
        sys.exit()

    except socket.error:
        print("Connection error")
        sys.exit()

    # Checking time again
    t2 = datetime.now()

    # calculate total time
    total = t2 - t1

    print("Scanning Completed in: ", total)

def network_scan():


if __name__ == '__main__':
    print("Welcome to Hacktool")

    