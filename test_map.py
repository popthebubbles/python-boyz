def loadMap(model):

    model.x = 20
    model.y = 20

    model.unit_grid = Unit_Grid(20, 20)
    model.map = Map(20, 20)

    model.map.auto_complete()


