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
        self.profile.display()



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
        self.img = pyglet.resource.image("ProfileIMG.jpg")
        self.menu = Menu()
        self.unit_info = Unit_Info()
    
    def update(self, unit):
        self.unit_info.update(unit)
    
    def display(self):
        self.img.blit(800, 0)
        self.menu.display()
        self.unit_info.display()


class Menu:
    def __init__(self):
        self.buttons = []
        
        #will generalize in later update?
        self.buttons.append(Menu_Button(800, 0, "End Turn", "ButtonIMG.gif"))
        self.buttons.append(Menu_Button(800, 67, "Item", "ButtonIMG.gif"))
        self.buttons.append(Menu_Button(800, 134, "Move", "ButtonIMG.gif"))
        self.buttons.append(Menu_Button(800, 201, "Attack", "ButtonIMG.gif"))

    def display(self):
        for x in self.buttons:
            x.display()


class Menu_Button:
    def __init__(self, x, y, text, img):
        self.x = x
        self.y = y
        
        self.sprite = pyglet.sprite.Sprite(pyglet.resource.image(img), x=x, y=y)
        self.label = pyglet.text.Label(text,
                          font_name='Times New Roman',
                          font_size=12,
                          x=x, y=y, color = (0, 0, 0, 255))

    def display(self):
        self.sprite.draw()
        self.label.draw()

class Unit_Info:
    def __init__(self):
        self.stat_bars = []
        
        self.stat_bars.append(Stat_Bar(800, 333, 'hp', 'Hit Points: '))
        self.stat_bars.append(Stat_Bar(800, 363, 'strength', 'Strength: '))
        self.stat_bars.append(Stat_Bar(800, 393, 'speed', 'Speed: '))
        self.stat_bars.append(Stat_Bar(800, 423, 'dexterity', 'Dexterity: '))
        self.stat_bars.append(Stat_Bar(800, 453, 'crit_chance', 'Crit. Chance: '))
        self.stat_bars.append(Stat_Bar(800, 483, 'armor', 'Armor: '))
        self.stat_bars.append(Stat_Bar(800, 513, 'move', 'Move: '))
    
    
        #Display Team info
        self.team_label = pyglet.text.Label('', font_name='Times New Roman', font_size=12, x=900, y = 543)
        
        
    def update(self, unit):
        for stat_bar in self.stat_bars:
            stat_bar.update(unit)

        if unit:
            self.team_label.text = unit.controller
        else:
            self.team_label.text = ''

    def display(self):
        for stat_bar in self.stat_bars:
            stat_bar.display()
        self.team_label.draw()

class Stat_Bar:
    def __init__(self, x, y, type, msg):
        self.msg = msg #e.g. 'Dexterity: '
        self.type = type #e.g. 'dexterity'
        self.x = x
        self.y = y
        self.stat = ''
        self.label = pyglet.text.Label(msg, font_name='Times New Roman', font_size=12,x=x, y=y)

    def update(self, unit):
        #print('updating unit')
        if unit:
            #print('unit detected')
            self.label.text = self.msg + str(unit.stats[self.type]) #e.g. 'Dexterity: 40'
        else:
            #print('no unit')
            self.label.text = self.msg #e.g. 'Dexterity: '

    def display(self):
        self.label.draw()

