from .cells import Wall, Ground
from .grid import Grid
from .player import Player
from .rect import Rectangle

class Dungeon:
    """
        this class will evolve to become the logic for actions
        to perform in the dungeon, manipulated by game.
        There will be a seperate object for generating cells, 
        and a constructor here will accept a grid.
        Think of it like Dungeon is the dungeon as it currently
        exists, inclusive of changes and current state. """

    def __str__(self):
        display = self.grid.add_grids(self.player.grid)
        return str(display)

    def __init__(self, width, height, room_generator):
        self.player = Player(6, 7)
        self.rooms = room_generator.generate()
        self.grid = self.make_grid(width, height)

    def make_grid(self, width, height):
        grid_rect = Rectangle(0, height, 0, width)
        grid = Grid(grid_rect, lambda:Wall())
        for room in self.rooms:
            grid = grid.add_grids(room, room.rect.left, room.rect.top)
        return grid


    def update_player(self, addx, addy):
        if not self.collide(addx, addy):
            self.player.update(addx, addy)

    def collide(self, addx, addy):
        new_x = self.player.x + addx
        new_y = self.player.y + addy
        return self.grid.cells[new_y][new_x].collides()


