# To run the client...
# python pingclient.py <host> [-i wait]

import sys
import time
from socket import *

# Check if the length of the command line args is 2
if len(sys.argv) == 2 or len(sys.argv) == 4:
	# Default wait in seconds
	wait = 1
	# Check if the option wait was specified
	if len(sys.argv) == 4:
		# Check for -i
		if str(sys.argv[2]) != "-i":
			print("Incorrect wait format. Use: [-i wait]")
			quit()
		# Check for a float greater than 0.1
		try:
			wait = float(sys.argv[3])
			if wait < 0.1:
				print("Wait specified was less than 0.1")
				quit()
		except ValueError:
			print("Wait specified was not an integer or fraction")
			quit()

	# Grab the hostname from the command line args
	serverName = str(sys.argv[1])
	serverPort = 5272
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	# Set the timeout for blocking operations to our wait in seconds
	clientSocket.settimeout(wait)

	# The message to send
	message = "PING"
	# Loop through 5 ping requests
	packetsLost = 0
	packetRTTs = []
	print("PING {}: 4 data bytes".format(serverName))
	for i in range(1,6):
		clientSocket.sendto(message.encode(), (serverName, serverPort))
		try:
			startTime = time.time() * 1000
			randomMessage, serverAddress = clientSocket.recvfrom(2048)
			endTime = time.time() * 1000
			# Grab and split the message code and random number received from the server
			randomMessageString = randomMessage.decode()
			if randomMessageString == "GNIP":
				# Find the difference in the sent and received time for RTT
				RTT = endTime - startTime
				print("4 bytes from {}: time={:.3f} ms".format(serverName, RTT))
				packetRTTs.append(RTT)
		except timeout:
			packetsLost += 1
	
	# Ping statistics
	packetsReceived = 5 - packetsLost
	print("--- {} Ping Statistics ---".format(serverName))
	if len(packetRTTs) > 0:
		print("5 packets transmitted, {} packets received, {:.2%} packet loss".format(packetsReceived,(packetsLost / 5)))
		print("round-trip min/avg/max = {:.3f}/{:.3f}/{:.3f} ms".format(
			min(packetRTTs),
	        (sum(packetRTTs) / packetsReceived),
	        max(packetRTTs))
	    )
	else:
		# Separate check to prevent errors of an empty packetRTTs list
		print("5 packets transmitted, {} packets received, {:.2%} packet loss".format(packetsReceived,(packetsLost / 5)))
		print("round-trip min/avg/max = {:.3f}/{:.3f}/{:.3f} ms".format(0,0,0))
	
	clientSocket.close()
else:
	print("Please use the format: python pingclient.py <host> [-i wait]")