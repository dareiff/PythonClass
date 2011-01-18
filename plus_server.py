import socket
import sys

# HOST = 'http://block115396-r76.blueboxgrid.com/'
HOST = ''
PORT = 40008

s = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

def addedFunction(receivedString):
	newString = receivedString.split(',')
	return newString

while 1:
	data = conn.recv(1024)
	if not data: break
	conn.send(addedFunction)
	
# print 'Variables received: %s and %s' % 

conn.close()