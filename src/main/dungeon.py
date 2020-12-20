from .cells import Wall, Ground
from .grid import Grid
from .player import Player

class Dungeon:
    """ todo: extract world shard base class
        create method to stamp on on top of other
        params x and y starting point
        dont go over edge of bottom shard """

    def __str__(self):
        grid = self.grid
        for room, x, y in self.rooms:
            grid = grid.add_grids(room, x, y)
        grid = grid.add_grids(self.player.grid, self.player.x, self.player.y)
        return str(grid)

    def __init__(self, width, height):
        self.grid = Grid(width, height, lambda:Wall())
        self.rooms = [
            (Grid(10, 5, lambda:Ground()), 3, 6),
            (Grid(6, 9, lambda:Ground()), 20, 5),
            (Grid(11, 3, lambda:Ground()), 27, 13)
        ]
        self.player = Player(6, 7)

    def update_player(self, addx, addy):
        self.player.x = self.player.x + addx
        self.player.y = self.player.y + addy

