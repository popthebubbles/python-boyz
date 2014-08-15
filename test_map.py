import game_model

def loadMap(model):

    model.x = 20
    model.y = 20

    model.unit_grid = game_model.Unit_Grid(20, 20)
    model.map = game_model.Map(20, 20)
    model.map.img = "background.png"

    model.map.auto_complete()


    thief = Thief()
    thief.team = 1
    thief1 = Thief()
    thief1.team = 1
    thief2 = Thief()
    thief2.team = 2
    thief3 = Thief()
    thief3.team = 2

    model.unit_grid.place_unit(5,5,thief)
    model.unit_grid.place_unit(5,6,thief1)
    model.unit_grid.place_unit(5,7,thief2)
    model.unit_grid.place_unit(5,8,thief3)



class Thief():
    def __init__(self):
        self.map_sprite_link = "Thief.png"
        self.portraint_sprite_link = None
        self.x = None
        self.y = None
        self.stats = {}
        self.stats['hp'] = 50
        self.stats['strength'] = 10
        self.stats['speed'] = 60
        self.stats['dexterity'] = 60
        self.stats['crit_chance'] = 30
        self.stats['armor'] = 10
        self.stats['move'] = 7
        self.controller = None
        self.move = 7 #for backwards compatibility... fix this later?
        self.moved = False
        self.team = None
