import pyglet

class View:
    def __init__(self, model):
        self.x = model.x
        self.y = model.y
        self.model = model
        self.grid = Display_Grid(model.x, model.y, model.unit_grid)
        self.profile = Profile()
        
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
    
        for x in range(self.x):
            for y in range(self.y):
                if model.unit_grid.grid[x][y]:
                    img = pyglet.resource.image(model.unit_grid.grid[x][y].map_sprite_link)
                    temp = pyglet.sprite.Sprite(img, x = 40*x, y = 40*y, batch=self.batch)
                    self.sprites.append(temp)
                    self.model.unit_grid.grid[x][y].sprite = temp


    def display(self):
        for x in range(self.x):
            for y in range(self.y):
                
                if self.grid.grid[x][y].highlit:
                    
                    img = pyglet.resource.image(self.grid.grid[x][y].img)
                    img.blit( 40 * x, 40 * y)

        self.batch.draw()

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

    def update(self):
        unit_grid = self.unit_grid
        for i in range(unit_grid.x):
            for j in range(unit_grid.y):
                if unit_grid.grid[i][j] == None:
                    self.grid[i][j].occupied = False
                else:
                    self.grid[i][j].occupied = True
                    #self.grid[i][j].img = unit_grid.grid[i][j].map_sprite_link
                    unit_grid.grid[i][j].sprite.x = 40 * i
                    unit_grid.grid[i][j].sprite.y = 40 * j
                    

    def turn_off_all(self):
        for i in range(self.x):
            for j in range(self.y):
                self.grid[i][j].turn_off_light()

    def highlight_valid_moves(self, moves):
        self.turn_off_all()
        for x in moves:
            self.grid[x[0]][x[1]].turn_on_light()
        
class Square:

    def __init__(self):
        self.highlit = False
        self.occupied = False
        self.img = "square.jpg"

    def turn_off_light(self):
        self.highlit = False

    def turn_on_light(self):
        self.highlit = True

class Profile:
    def __init__(self):
        pass
    def update(self):
        pass
