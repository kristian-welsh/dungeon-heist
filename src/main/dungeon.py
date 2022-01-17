from .cells import Wall, Ground
from .grid import Grid
from .player import Player
from .enemy import Enemy
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
        display = self.grid
        display = display.add_grids(self.player.grid)
        display = display.add_grids(self.enemy.grid)
        return str(display)

    def __init__(self, width, height, room_generator):
        # spawn player inside guarenteed room for testing
        self.player = Player(6, 7)
        test_room = Grid(Rectangle(5, 15, 5, 15), lambda:Ground())
        self.enemy = Enemy(7, 9)

        rooms = room_generator.generate()
        rooms.append(test_room)
        self.grid = self.make_grid(width, height, rooms)

    def make_grid(self, width, height, rooms):
        grid = Grid(Rectangle(0, height, 0, width), lambda:Wall())
        for room in rooms:
            grid = grid.add_grids(room)
        return grid

    def update_player(self, addx, addy):
        if not self.collide(addx, addy):
            self.player.update(addx, addy)

    def update_enemy(self, addx, addy):
        pass

    def collide(self, addx, addy):
        """remember, this only collides against self.grid, not all entities"""
        new_x = self.player.x + addx
        new_y = self.player.y + addy
        return self.grid.cells[new_y][new_x].collides()


