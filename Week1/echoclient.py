import socket
import time

host = 'block115396-r76.blueboxgrid.com'
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.send("Hello, world.")
	data = s.recv(1024)
	s.close()
	print data
	time.sleep(6)
