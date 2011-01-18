import socket
import sys

HOST = 'http://block115396-r76.blueboxgrid.com/'
PORT = 40008

s = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)