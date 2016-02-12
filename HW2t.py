import socket

UDP_IP="169.254.100.62"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
	rspd, addr = sock.recvfrom(1024) # buffer size = 1024 bytes
	print "rspd:", rspd
	lspd, addr = sock.recvfrom(1024) # buffer size = 1024 bytes
	print "rspd:", lspd


