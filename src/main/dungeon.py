from .cells import Wall, Ground
from .grid import Grid

class Dungeon:
    """ todo: extract world shard base class
        create method to stamp on on top of other
        params x and y starting point
        dont go over edge of bottom shard """

    def __str__(self):
        return str(self.grid)

    def __init__(self, width, height):
        self.grid = Grid(width, height, lambda:Wall())
        room1 = Grid(10, 5, lambda:Ground())
        room2 = Grid(6, 9, lambda:Ground())
        room3 = Grid(11, 3, lambda:Ground())
        self.grid = self.grid.add_grids(room1, 3, 6)
        self.grid = self.grid.add_grids(room2, 27, 13)
        self.grid = self.grid.add_grids(room3, 20, 5)
