
class controller:

    def __init__(self, s):
		pass

	# 20 x 20 grid, 40x40 size boxes, 67 3 buttons 3/3
    def mouse_click_dispatch(self, x, y):
        if(x > 800 and x < 1100 and y > 534 and y < 800):
            boiz = 534
            countery = 0
            while boiz < y:
                boiz +=67
                countery +=1
        
            self.action(countery)
        else:
           boiz = 40
           counterx = 0
           while boiz < x:
               boiz += 40
               counterx += 1
           boiz = 40
           countery = 0
           while boiz < y:
               boiz += 40
               countery += 1
        self.select(counterx, countery)

    def update_view():
        pass

    def update_server():
        pass

    def update_model():
        pass

    def players_turn():
        pass

    def select(self, x, y):
        pass

    def move():
        pass

    def attack():
        pass

    def battle():
        pass

    def kill():
        pass

    def trigger():
        pass

    def recv_move():
        pass
    
    def action(self, num):
        pass
