import socket

#Socket = Endpoint of a connection that is responsible for receiving data
#A socket has a hostname and a port number attached 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = IPv4
#SOCK_STREAM = TCP
s.connect((socket.gethostname(),1234))

mess = ''
while True:
	message = s.recv(8)
	if len(message) <= 0:
		break
	mess  += message.decode('utf-8')
#s.recv is to recieve the incoming data from the server
#1024 is the specified byte size of the incoming data
print(mess)