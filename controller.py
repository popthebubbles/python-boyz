
class Controller:

    def __init__(self, s, view, model):
        self.s = self
        self.view = view
        self.model = model
        self.action = False
    
	# 20 x 20 grid, 40x40 size boxes, 67 3 buttons 3/3
    def mouse_click_dispatch(self, x, y):
        
        #print 'Click at:', x, y
        
        if(x > 800 and x < 1100):
            if(y > 534 and y < 800):
                increment = 534
                countery = 0
                while increment < y:
                    increment +=67
                    countery +=1
            
                print "Output", countery
                self.action(countery)
        elif x < 800 and x > 0 and y < 800 and y > 0:
           increment = 40
           counterx = 0
           while increment < x:
               increment += 40
               counterx += 1
           increment = 40
           countery = 0
           while increment < y:
               increment += 40
               countery += 1
            
           print "Output:", counterx, countery
           self.select(counterx, countery)

    def update_view(self):
        if self.model.selected == None:
            self.view.grid.turn_off_all()
        else:
            self.view.grid.highlight_valid_moves(self.model.path(self.model.unit_grid, self.model.map, self.model.selected))
        self.view.grid.update()
        self.view.profile.update()

    #needs implementing
    def update_server(msg, x1, y1, x2, y2):
        s.send(msg + ' ' + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2)

    def players_turn():
        pass

    def select(self, x, y):
        
        print('selected')
        #if an action has been selected
        if self.action and self.model.selected:
            if self.action == 1:
                #self.action = False
                self.attack(x,y)
            if self.action == 2:
                #self.action = False
                self.move(x,y,self.model.selected)
        else:
            self.model.selected = self.model.unit_grid.grid[x][y]
        
        self.update_view()

    def move(self, x, y, unit):
        
        moves = self.model.path(self.model.unit_grid, self.model.map, unit)
        print(moves)

        if (x,y) in moves:
            self.model.unit_grid.mov_unit(unit, unit.x, unit.y, x, y)
            self.update_view()

        self.model.selected = None

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
