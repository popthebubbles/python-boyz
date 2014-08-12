class View:
    def __init__(self, model):
        self.display_grid = Display_Grid(model.x, model.y, model.unit_grid)
        self.profile = Profile()

class Display_Grid:

    def __init__(self, x, y, unit_grid):
        grid = []
        self.x = x
        self.y = y
        self.unit_grid = unit_grid
        for i in range(x):
            grid.append([])
            for j in range(y):
                grid[i].append(Square())
        self.grid = grid

    def update(self)
        unit_grid = self.unit_grid
        for i in range(unit_grid.x):
            for j in range(unit_grid.y):
                if unit_grid[x][y] == None:
                    self.grid[x][y].occupied = False
                    self.grid[x][y].unitimg = None
                else:
                    self.grid[x][y].occupied = True
                    self.grid[x][y].unitimg = unit_grid[x][y].map_sprite_link

    def turn_off_all(self):
        for i in range(self.x):
            for j in range(self.y):
                self.grid[i][j].turn_off_light()

    def hightlight_valid_moves(self, moves):
        self.turn_off_all()
        for x in moves:
            self.grid[x[0]][x[1]].turn_on_light()
        
class Square:

    def __init__(self):
        highlit = False
        occupied = False
        unitimg = None

    def turn_off_light(self):
        highlit = False

    def turn_on_light(self):
        highlit = True

class Profile:
    def __init__(self):
        pass
    def update(self):
        pass
