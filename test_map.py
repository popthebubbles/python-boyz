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
    thief1 = game_model.Unit()
    thief1.map_sprite_link = "Dragon.png"
    thief2 = game_model.Unit()
    thief2.map_sprite_link = "Dragon.png"
    thief3 = game_model.Unit()
    thief3.map_sprite_link = "Dragon.png"

    model.unit_grid.place_unit(5,5,thief)
    model.unit_grid.place_unit(5,6,thief1)
    model.unit_grid.place_unit(5,7,thief2)
    model.unit_grid.place_unit(5,8,thief3)
