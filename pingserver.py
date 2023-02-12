# To start the server...
# python pingserver.py

from socket import *

# Set up the socket 
serverPort = 5272
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
# Set to a non-blocking receive with exception handling.
# This isn't really necessary but it allows Windows to Ctrl + C and kill the program.
# Blocking mode won't allow that.
serverSocket.setblocking(0)

print("Server is ready to receive...")
while True:
    try:
        # Receive a message from a client
        message, clientAddress = serverSocket.recvfrom(2048)
        
        # Split the message into its sections
        messageString = message.decode()
        # Check if the message sent was PING
        if messageString == "PING":
            # Send the reversed string back
            modifiedMessage = "GNIP"
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    except BlockingIOError:
        pass
