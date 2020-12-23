from .cells import Wall, Ground
from .grid import Grid
from .player import Player

class Dungeon:
    """ todo: extract world shard base class
        create method to stamp on on top of other
        params x and y starting point
        dont go over edge of bottom shard
        
        this class will evolve to become the logic for actions
        to perform in the dungeon, manipulated by game.
        There will be a seperate object for generating cells, 
        and a constructor here will accept a grid.
        Think of it like Dungeon is the dungeon as it currently
        exists, inclusive of changes and current state. """

    def __str__(self):
        grid, x, y = (self.player.grid, self.player.x, self.player.y)
        display = self.grid.add_grids(grid, x, y)
        return str(display)

    def __init__(self, width, height):
        self.player = Player(6, 7)
        self.rooms = [
            (Grid(10, 5, lambda:Ground()), 3, 6),
            (Grid(6, 9, lambda:Ground()), 20, 5),
            (Grid(11, 3, lambda:Ground()), 27, 13),
        ]
        self.grid = self.make_grid(width, height)

    def make_grid(self, width, height):
        grid = Grid(width, height, lambda:Wall())
        for room, x, y in self.rooms:
            grid = grid.add_grids(room, x, y)
        return grid


    def update_player(self, addx, addy):
        if not self.collide(addx, addy):
            self.player.update(addx, addy)

    def collide(self, addx, addy):
        new_x = self.player.x + addx
        new_y = self.player.y + addy
        return self.grid.cells[new_y][new_x].collides()

