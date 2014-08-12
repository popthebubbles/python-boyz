python-boyz
===========
This is a collaborative game project written by the Python code instructors at SummerTech

Game Architecture:
==================


Each client has it's own model, view, and controller
The client model handles the user inputs and updates the view accordingly

Essentially:
view constantly updates based on the client model
controller feeds input to client model
client controller talks to server
server model updates
server pushes changes to client controllers
controllers update the client models
