#has to display and read input, pass input along to server
#will client have to multithread in order to talk to server and do graphics??
import view
import controller
import thread
import socket

ip = 'localhost'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

#Make the view and controller
view = view.View()

#controller takes the socket as input so it can communicate w/ server
controller = controller.Controller(s)




s.close()