
class Controller:

    def __init__(self, s, view, model):
        self.s = self
        self.view = view
        self.model = model
    
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
        if self.model.selected == None:
            self.view.display_grid.turn_off_all()
        else:
            self.view.display_grid.highlight_valid_moves(self.model.path(self.model.selected))

        self.view.display_grid.update()
        self.view.profile.update()

    #needs implementing
    def update_server(msg, x1, y1, x2, y2):
        s.send(msg + ' ' + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2)

    def players_turn():
        pass

    def select(self, x, y):
        self.model.selected = self.model.unit_grid[x][y]
        self.update_view()

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
