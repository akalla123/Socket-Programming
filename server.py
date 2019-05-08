import socket

#Socket = Endpoint of a connection that is responsible for receiving data
#A socket has a hostname and a port number attached 
a = input("Say Something to the Client: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = IPv4
#SOCK_STREAM = TCP

s.bind((socket.gethostname(),1234))
#gethostname = HostName (LocalHost)
#1234 = Port Number

s.listen(5)
#make a queue to hold 5 requests at once
while True:
	clientsocket, address = s.accept()
	#establish connection to the client
	#hostname and address of client socket
	print(f"Connection with {address} has been established")
	clientsocket.send(bytes(a,'utf-8'))
	#Send message to client socket once connection is established
	clientsocket.close()
	#Close connection once you send the message