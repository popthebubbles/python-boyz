#has to display and read input, pass input along to server

import socket

ip = 'localhost'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
