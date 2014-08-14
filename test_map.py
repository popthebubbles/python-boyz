import game_model

def loadMap(model):

    model.x = 20
    model.y = 20

    model.unit_grid = game_model.Unit_Grid(20, 20)
    model.map = game_model.Map(20, 20)
    model.map.img = "background.png"

    model.map.auto_complete()


    thief = game_model.Unit()
    thief.map_sprite_link = "Dragon.png"
    thief.move = 7
    thief.team = 1
    thief.stats['move'] = 7
    thief.stats['hp'] = 50
    thief.stats['strength'] = 10
    thief.stats['speed'] = 60
    thief.stats['dexterity'] = 60
    thief.stats['crit_chance'] = 30
    thief.stats['armor'] = 10
    
    thief1 = game_model.Unit()
    thief1.map_sprite_link = "Dragon.png"
    thief1.move = 7
    thief1.team = 1
    thief2 = game_model.Unit()
    thief2.map_sprite_link = "Dragon.png"
    thief2.move = 7
    thief2.team = 2
    thief3 = game_model.Unit()
    thief3.map_sprite_link = "Dragon.png"
    thief3.move = 7
    thief3.team = 2

    model.unit_grid.place_unit(5,5,thief)
    model.unit_grid.place_unit(5,6,thief1)
    model.unit_grid.place_unit(5,7,thief2)
    model.unit_grid.place_unit(5,8,thief3)

    