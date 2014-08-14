
class Controller:

    def __init__(self, s, view, model, team):
        self.s = self
        self.view = view
        self.model = model
        self.action = False
        self.team = team
    
	# 20 x 20 grid, 40x40 size boxes, 67 3 buttons 3/3
    def mouse_click_dispatch(self, x, y):
        
        #print 'Click at:', x, y
        
        if(x > 800 and x < 1100):
            if(y > 0 and y < int(800/3)):
                increment = int(800/3)
                countery = 0
                while increment > y:
                    increment -=67
                    countery +=1
                
                print "Output", countery
                self.menu_click(countery)
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
            if not self.model.selected.moved:
                self.view.grid.highlight_valid_moves(self.model.path(self.model.unit_grid, self.model.map, self.model.selected))
        self.view.grid.update()
        self.view.profile.update(self.model.selected)

    #needs implementing
    def update_server(msg, x1, y1, x2, y2):
        s.send(msg + ' ' + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2)

    def players_turn():
        pass

    def select(self, x, y):
        #if an action has been selected
        if self.action and self.model.selected:
            if self.action == 1:
                self.action = False
                self.attack(x,y)
            if self.action == 2:
                self.action = False
                self.move(x,y,self.model.selected)
        else:
            if self.model.unit_grid.grid[x][y]:
                if self.model.unit_grid.grid[x][y].team == self.team:
                    self.model.selected = self.model.unit_grid.grid[x][y]
            else:
                self.model.selected = None

        self.update_view()

    def move(self, x, y, unit):
        
        moves = self.model.path(self.model.unit_grid, self.model.map, unit)
        #print(moves)

        if (x,y) in moves and not unit.moved:
            self.model.unit_grid.mov_unit(unit, unit.x, unit.y, x, y)
            self.update_view()
            unit.moved = True

        self.model.selected = None

    def attack():
        #apply combat formula based on stats
        pass

    def battle():
        pass

    def kill():
        #remove from player grid, delete unit
        pass

    def trigger():
        #leave unimplemented for version 1.0
        pass

    def recv_move():
        #idk, Nathan is handling server communication
        pass
    
    def menu_click(self, num):
        self.action = num