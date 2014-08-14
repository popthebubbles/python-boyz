#has to display and read input, pass input along to server
#will client have to multithread in order to talk to server and do graphics??
import view
import controller
import thread
import socket
import pyglet
import game_model

#ip = 'localhost'
#port = 8888

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((ip, port))
s=0

#Make the view and controller

model = game_model.Model()
view = view.View(model)


#controller takes the socket and view as inputs

con = controller.Controller(s, view, model, 1)

window = pyglet.window.Window(1100,800)
image = pyglet.resource.image(model.map.img)

@window.event
def on_mouse_release(x, y, button, modifiers):
    #needs to get lock before dispatching, handle here
    con.mouse_click_dispatch(x,y)

@window.event
def on_draw():
    window.clear()
    
    image.blit(0,0)
    
    view.display()

pyglet.app.run()


#s.close()



#waitforturn()
#new thread

#rec_move()
#receives an opponents action from the server
#when received, gets lock
#changes board, frees lock


#sendmove()

#getteam()

#Please do this Nathan. 

