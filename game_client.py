#has to display and read input, pass input along to server
#will client have to multithread in order to talk to server and do graphics??
import view
import controller
import thread
import socket
import pyglet
import game_model

ip = 'localhost'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

#Make the view and controller
view = view.View()

model = game_model.Model()



#controller takes the socket and view as inputs

controller = controller.Controller(s, view, model)

window = pyglet.window.Window()




s.close()