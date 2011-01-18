import socket
import sys

# HOST = 'http://block115396-r76.blueboxgrid.com/'
HOST = ''
PORT = 40008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)

def addedFunction(receivedString):
	print receivedString
	newString = receivedString.split(',')
	return newString

while True:
	conn, addr = s.accept()
	data = conn.recv(1024)
	conn.send(addedFunction(data))
	
# print 'Variables received: %s and %s' % 

conn.close()