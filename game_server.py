import socket
import sys
from thread import *


HOST = ''
PORT = 8888 #Abitrary Port

#creates a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'

try:
    #binds to a port
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Failed to bind. Error Code: ' + str(msg[0]) + '. Error Message: ' + str(msg[1])
    sys.exit()

print 'Socket bind complete'

s.listen(10) #tells to listen and sets backlog
print 'Socket now listening'

#Function for handling connections
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n')
    
    #infinite loop so that function does not terminate and threads do not end
    while True:
        
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break
        
        conn.sendall(reply)
    
    #came out of loop
    conn.close()



#now keep talking with client
while True:
    #wait to accept a connection- blocking call
    conn, addr = s.accept()
    
    #display client information
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

s.close()