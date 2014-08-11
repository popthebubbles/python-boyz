from Game_Model import *

unit_grid = Unit_Grid(20, 20)
map = Map(20, 20)

map.auto_complete()

unit = Unit()
unit.move = 3

unit_grid.place_unit(9, 9, unit)

x = path(unit_grid, map, unit)
print x