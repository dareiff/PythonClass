import socket
import sys

HOST = 'block115396-r76.blueboxgrid.com/'
# HOST = ''
PORT = 40008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send('1,5')
data = s.recv(1024)
print 'Received:', repr(data)
s.close()