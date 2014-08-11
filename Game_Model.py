#Establishes the game model: classes for map, units, combat

class Unit_Grid:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.grid = []
        for i in range(x):
            self.grid.append([])
            for j in range(y):
                self.grid[i].append(None)

    def place_unit(self, x, y, unit):
        if self.grid[x][y] == None:
            self.grid[x][y] = unit
            unit.x_pos = x
            unit.y_pos = y
        else:
            print('Invalid unit placement')

    def mov_unit(self, unit, x1, y1, x2, y2):
        self.grid[x2][y2] = self.grid[x1][y1]
        self.grid[x1][y1] = None
        unit.x = x2
        unit.y = y2

class Map:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.map = []
        for i in range(x):
            self.map.append([])
            for j in range(y):
                self.map[i].append(None)
    
    #set the rest of the map terrain
    def auto_complete(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.map[i][j] == None:
                    self.map[i][j] = Terrain()

class Terrain:
    def __init__(self):
        self.mov_effect = False
        self.status_effect = []

    #sets the movement impediments of the map, important for pathing
    def set_mov_effect(self, effect):
        if effect == 'up' or effect == 'down' or effect == 'left' or effect == 'right' or effect == 'no':
            self.move_effect = effect
        else:
            print 'Invalid move effect: ', effect

    #sets status effect. Status effects can be custom so no checking
    #effect is a list for status effect!!!
    def set_status_effect(self, effect):
        self.status_effect = effect

#Super class for all unit types, individual units must be derived
#Units can have hp, strength, speed, dexterity, crit chance, armor, movement
#sprites for their portrait view and their map representation

class Unit:
    def __init__(self):
        self.map_sprite_link = None
        self.portraint_sprite_link = None
        self.x_pos = None
        self.y_pos = None
        self.hp = None
        self.strength = None
        self.speed = None
        self.dexterity = None
        self.crit_chance = None
        self.armor = None
        self.move = None


#returns a list of x,y tuples, the valid squares you can move
def path(grid, map, unit):
    model = []
    x = unit.x_pos
    y = unit.y_pos
    for i in range(map.x):
        model.append([])
        for j in range(map.y):
            model[i].append(True)

    start = (unit.x_pos, unit.y_pos, unit.move)
    valid_moves = []

    #hot fix
    grid.grid[unit.x_pos][unit.y_pos] = None
    model[unit.x_pos][unit.y_pos] = False

    queue = [start]

    while queue:

        temp = queue.pop(0)
        
        #check to see if the square is empty
        if grid.grid[temp[0]][temp[1]] == None:
            #check terrain
            if not map.map[temp[0]][temp[1]].mov_effect == 'no':
                #square is valid, add it to list of valid moves
                valid_moves.append(temp)

                #now we check for other possible moves
                #if you have moves add more possible squares
                if temp[2] > 0:
                    if (not map.map[temp[0]][temp[1]] == 'up') and temp[0] - 1 > 0:
                        if model[temp[0] - 1][temp[1]]:
                            queue.append( (temp[0] - 1, temp[1], temp[2] - 1))
                            model[ temp[0] - 1][ temp[1] ] = False
                    
                    if (not map.map[temp[0]][temp[1]] == 'down') and temp[0] + 1 < map.x:
                        if model[temp[0] + 1][temp[1]]:
                            queue.append( (temp[0] + 1, temp[1], temp[2] - 1))
                            model[ temp[0] + 1][ temp[1] ] = False
                

                    if (not map.map[temp[0]][temp[1]] == 'left') and temp[1] - 1 > 0:
                        if model[temp[0]][temp[1] - 1]:
                            queue.append( (temp[0], temp[1] - 1, temp[2] - 1))
                            model[ temp[0] ][ temp[1] - 1 ] = False

                    if (not map.map[temp[0]][temp[1]] == 'right') and temp[1] + 1 < map.y:
                        if model[temp[0]][temp[1] + 1]:
                            queue.append( (temp[0], temp[1] + 1, temp[2] - 1))
                            model[ temp[0] ][ temp[1] + 1 ] = False



    # hot fix
    grid.grid[unit.x_pos][unit.y_pos] = unit

    return valid_moves




