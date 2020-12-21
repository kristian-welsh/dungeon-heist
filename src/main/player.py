from .grid import Grid
from .cells import PlayerCell

class Player():

    def update(self, addx, addy):
        self.x = self.x + addx
        self.y = self.y + addy

    def __init__(self, x, y):
        """
        grid is really becoming something like Sprite
        i guess grid is really sprite, and its current default constructor 
        draws a rectangle in that sprite of width by height.
        I guess that means Dungeon isuStage
        """
        self.grid = Grid(1, 1, lambda: PlayerCell())
        self.x = x
        self.y = y
