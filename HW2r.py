import socket

UDP_IP = "169.254.100.62"
UDP_PORT = 5005
#MESSAGE = "Hello, this is Robot!"
rspd="500"
lspd="500"



print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
while True:

	sock.sendto(rspd, (UDP_IP, UDP_PORT))
	sock.sendto(lspd, (UDP_IP, UDP_PORT))
	#print "speed:", rspd,lspd

